// Reihenkämpfe: jede Fraktion gegen mehrere Armee-Typen, vom Spiel selbst gespielt (Automatik wie
// nach dem Tod des Lichs). Misst Siegquote und Verluste, mit und ohne Doktrin der Fraktion.
// Aufruf: node tools/test/matrix.js [Verhältnis 1.3] [Stunde 12] [Orte je Fraktion 3] [Teil k/n, z. B. 1/2] [Fraktionen, Komma oder -] [easy|normal|hard]
// Ausgabe: eine JSON-Zeile je Kampf, am Ende eine Tabelle. Armee-Stärke = Verhältnis × Stärke der
// Besatzung ohne Doktrin (Campaign.strength), alle Verteidiger sind gewarnt (kein Schleichen).
const { chromium } = require('playwright'); const fs = require('fs'), path = require('path');
const REPO = path.join(__dirname, '..', '..'), SP = __dirname;
const RATIO = +(process.argv[2] || 1.3), HOUR = +(process.argv[3] || 12), PER = +(process.argv[4] || 3), PART = (process.argv[5] || '1/1').split('/').map(Number), ONLY = process.argv[6] && process.argv[6] !== '-' ? process.argv[6].split(',') : null, LEVEL = process.argv[7] || 'normal';
(async () => {
  const br = await chromium.launch(); const pg = await br.newPage(); const errs = [];
  pg.on('pageerror', e => errs.push(e.message + ' ' + (e.stack || '').split('\n').slice(1, 3).join(' | ')));
  pg.on('console', m => { if (m.text().startsWith('ROW ')) console.log(m.text().slice(4)); });
  await pg.route('https://cdn.jsdelivr.net/**', r => { const u = r.request().url(); r.fulfill({ contentType: 'application/javascript', body: fs.readFileSync(path.join(SP, u.includes('CSS2D') ? 'css2d.js' : u.includes('GLTFLoader') ? 'gltf.js' : 'three.js')) }); });
  await pg.route('**/index.html', r => { let h = fs.readFileSync(path.join(REPO, 'index.html'), 'utf8'); const i = h.lastIndexOf('</script>');
    h = h.slice(0, i) + '\nwindow.__T = { Battle, Campaign, Doctrine, game, newGame, DATA, Figures, NODE_BY_ID, Narrator, UI, Sfx, stackCount, SaveGame };\n' + h.slice(i);
    h = h.replace('tw.t += dt * (tw.fast && game.hurry ? 4 : 1);', 'tw.t += 99;').replace(/const AI_PAUSE = [\d.]+/, 'const AI_PAUSE = 0')
      .replace("if (u.side === 'player' && !b.auto) {", "if (u.side === 'player' && !b.auto && !window.__auto) {");
    if (!h.includes('!window.__auto')) throw new Error('auto hook not found');
    r.fulfill({ contentType: 'text/html', body: h }); });
  await pg.goto('file://' + REPO + '/index.html'); await pg.waitForTimeout(6000);
  const res = await pg.evaluate(async ([RATIO, HOUR, PER, PART, ONLY, LEVEL]) => {
    const { Battle, Campaign, game, newGame, DATA, Figures, Narrator, UI, Sfx, stackCount, SaveGame } = window.__T; newGame();
    for (const t of Object.keys(DATA.units)) Figures.templates[t] = null;
    Narrator.hint = () => {}; Narrator.speak = () => {}; Narrator.say = () => {}; UI.toast = () => {}; UI.news = () => {}; SaveGame.save = () => {}; Sfx.muted = true;
    const ARMIES = {
      start:     { ghul: 3, skelett: 2 },
      masse:     { skelett: 5, zombie: 3, ghul: 2, knochentrommler: 0.3, seuchenvogt: 0.4 },
      klasse:    { todesritter: 5, fleischriese: 3, knochenschuetze: 2 },
      schatten:  { nachzehrer: 5, geist: 3, leichenhund: 2, nachtvogt: 0.6 },
      eile:      { leichenhund: 3, knochenreiter: 5, totenjaeger: 2 },
      bollwerk:  { gruftwaechter: 5, todesritter: 3, zombie: 2, gruftfuerst: 0.6 },
      hexerei:   { knochenhexer: 4, grabdruidin: 2, gefallene_schwester: 2, bogner: 2, nekromant: 0.6 }
    };
    const S = t => Campaign.strength([t]);
    const build = (W, target) => {
      const army = [{ type: 'lich', hp: DATA.units.lich.hp }], got = {}; let total = 0; const sum = Object.values(W).reduce((a, b) => a + b, 0);
      for (const [t, w] of Object.entries(W)) if (w < 1) { army.push({ type: t, hp: DATA.units[t].hp }); got[t] = S(t); total += S(t); }      // one commander / drummer
      for (let guard = 0; total < target && guard < 2000; guard++) {
        const t = Object.keys(W).filter(k => W[k] >= 1).sort((a, b) => (got[a] || 0) / W[a] - (got[b] || 0) / W[b])[0];
        army.push({ type: t, hp: DATA.units[t].hp }); got[t] = (got[t] || 0) + S(t); total += S(t);
      }
      return army;
    };
    const saved = {}; for (const [f, F] of Object.entries(DATA.factions)) saved[f] = F.doctrine;
    const setDoctrine = on => { for (const [f, F] of Object.entries(DATA.factions)) F.doctrine = on ? saved[f] : undefined; };
    const jobs = [];
    for (const f of Object.keys(DATA.factions)) {
      if (f === 'UNDEAD' || (ONLY && !ONLY.includes(f))) continue;
      const places = DATA.nodes.filter(n => n.faction === f && (n.size || 16) <= 32 && Object.keys(n.garrison || {}).length && !Object.keys(n.garrison).some(t => DATA.units[t].rank === 'UNIQUE'))
        .sort((a, b) => Object.values(a.garrison).reduce((x, y) => x + y, 0) - Object.values(b.garrison).reduce((x, y) => x + y, 0));
      const pick = []; for (let i = 0; i < PER; i++) { const p = places[Math.floor((i + 0.5) * places.length / PER)]; if (p && !pick.includes(p)) pick.push(p); }
      for (const node of pick) for (const a of Object.keys(ARMIES)) for (const doc of [true, false]) jobs.push({ f, node, a, doc });
    }
    const out = [];
    for (let j = 0; j < jobs.length; j++) {
      if (j % PART[1] !== PART[0] - 1) continue;
      const { f, node, a, doc } = jobs[j];
      newGame(); const c = game.campaign; c.hour = HOUR; c.nodeId = node.id; c.debugNoFog = true; c.difficulty = LEVEL;
      setDoctrine(false); const raw = Campaign.strength(Campaign.garrisonFor(node)); setDoctrine(doc);
      c.threat[f] = 60;                                                    // warned: a plain fight
      c.army = build(ARMIES[a], raw * RATIO);
      const rec = { f, node: node.id, army: a, doc, n: c.army.length, foe: Campaign.garrisonFor(node).length };
      const t0 = performance.now();
      try {
        window.__auto = true; await Battle.start(node); const b = game.battle;
        const P = () => b.units.filter(u => u.side === 'player');
        const st0 = P().reduce((s, u) => s + (u.startCount || stackCount(u)) * S(u.type), 0);
        let result = null; const fin = Battle.finish.bind(Battle); Battle.finish = r => { result = result || r; rec.rounds = b.round; rec.left = P().reduce((s, u) => s + (u.alive ? stackCount(u) : 0) * S(u.type), 0) / st0; Battle.finish = fin; fin(r); };
        for (let i = 0; i < 12000 && !b.over && b.round <= 40 && performance.now() - t0 < 90000; i++) await new Promise(r => setTimeout(r, 4));
        rec.result = result || (b.round > 40 ? 'timeout' : 'stuck r' + b.round); rec.lich = !!P().find(u => u.type === 'lich' && u.alive);
        if (!result) rec.left = P().reduce((s, u) => s + (u.alive ? stackCount(u) : 0) * S(u.type), 0) / st0;
        Battle.finish = fin; try { if (!b.over) b.over = true; Battle.exit(); } catch (e) { /* ignore */ }
      } catch (e) { rec.result = 'ERR ' + e.message; }
      UI.closeModal && UI.closeModal(); rec.ms = Math.round(performance.now() - t0); rec.left = rec.left === undefined ? null : +rec.left.toFixed(2);
      console.log('ROW ' + JSON.stringify(rec)); out.push(rec);
    }
    setDoctrine(true);
    return out; }, [RATIO, HOUR, PER, PART, ONLY, LEVEL]);
  // Summary: per faction win rate and army left, with and without doctrine.
  const F = {}; for (const r of res) { const k = r.f; F[k] = F[k] || { on: [], off: [] }; F[k][r.doc ? 'on' : 'off'].push(r); }
  const avg = (l, f) => l.length ? l.reduce((s, r) => s + f(r), 0) / l.length : 0;
  console.error(`\nVerhältnis ${RATIO}, ${HOUR} Uhr. Siegquote / übrige Armee (Anteil der Stärke), mit und ohne Doktrin`);
  for (const [k, v] of Object.entries(F)) console.error(k.padEnd(13), 'mit', (avg(v.on, r => r.result === 'victory') * 100).toFixed(0).padStart(3) + '%', avg(v.on, r => r.left || 0).toFixed(2), ' ohne', (avg(v.off, r => r.result === 'victory') * 100).toFixed(0).padStart(3) + '%', avg(v.off, r => r.left || 0).toFixed(2), ' n=' + v.on.length);
  if (errs.length) console.error('FEHLER:\n' + errs.slice(0, 5).join('\n'));
  await br.close(); })();

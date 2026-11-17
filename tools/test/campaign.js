// Kampagnen-Bot: spielt eine ganze Kampagne in einem Spielstil – baut, forscht, lernt Pfade,
// rekrutiert, reist und greift an. Die Kämpfe spielt die Automatik des Spiels (wie nach dem Tod
// des Lichs), also ohne Schleichen und ohne menschliches Geschick: Die Ergebnisse sind eher zu
// vorsichtig als zu günstig.
// Aufruf: node tools/test/campaign.js <stil> [Tage 150] [Mindestverhältnis 1.0] [Saat 1] [easy|normal|hard]
// Stile: gemischt, masse, klasse, schatten, eile, bollwerk, hexerei
// Ausgabe: JSON-Zeilen (battle / day), am Ende eine Zusammenfassung auf stderr.
const { chromium } = require('playwright'); const fs = require('fs'), path = require('path');
const REPO = path.join(__dirname, '..', '..'), SP = __dirname;
const STYLE = process.argv[2] || 'gemischt', DAYS = +(process.argv[3] || 150), MINRATIO = +(process.argv[4] || 1.0), SEED = +(process.argv[5] || 1), LEVEL = process.argv[6] || 'normal';
(async () => {
  const br = await chromium.launch(); const pg = await br.newPage(); const errs = [];
  pg.on('pageerror', e => errs.push(e.message + ' ' + (e.stack || '').split('\n').slice(1, 3).join(' | ')));
  pg.on('console', m => { if (m.text().startsWith('ROW ')) console.log(m.text().slice(4)); });
  await pg.route('https://cdn.jsdelivr.net/**', r => { const u = r.request().url(); r.fulfill({ contentType: 'application/javascript', body: fs.readFileSync(path.join(SP, u.includes('CSS2D') ? 'css2d.js' : u.includes('GLTFLoader') ? 'gltf.js' : 'three.js')) }); });
  await pg.route('**/index.html', r => { let h = fs.readFileSync(path.join(REPO, 'index.html'), 'utf8'); const i = h.lastIndexOf('</script>');
    h = h.slice(0, i) + '\nwindow.__T = { Difficulty, Fow, Battle, Campaign, Base, Upgrades, Skills, Recruitment, Knowledge, Raids, Stranded, game, newGame, DATA, Figures, NODE_BY_ID, PHYLACTERY, Narrator, UI, Sfx, SaveGame, stackCount, hexDistance, startTravel, resumeTravel, RECRUIT_AT };\n' + h.slice(i);
    h = h.replace('tw.t += dt * (tw.fast && game.hurry ? 4 : 1);', 'tw.t += 99;').replace(/const AI_PAUSE = [\d.]+/, 'const AI_PAUSE = 0')
      .replace("if (u.side === 'player' && !b.auto) {", "if (u.side === 'player' && !b.auto && !window.__auto) {");
    if (!h.includes('!window.__auto')) throw new Error('auto hook not found');
    r.fulfill({ contentType: 'text/html', body: h }); });
  await pg.goto('file://' + REPO + '/index.html'); await pg.waitForTimeout(6000);
  const res = await pg.evaluate(async ([STYLE, DAYS, MINRATIO, SEED, LEVEL]) => {
    const { Difficulty, Fow, Battle, Campaign, Base, Upgrades, Skills, Recruitment, Knowledge, Stranded, game, newGame, DATA, Figures, NODE_BY_ID, PHYLACTERY, Narrator, UI, Sfx, SaveGame, stackCount, hexDistance, startTravel } = window.__T;
    // Seeded randomness so that runs can be repeated.
    let seed = SEED * 7919 + 13; Math.random = () => { seed = (seed * 1664525 + 1013904223) >>> 0; return seed / 4294967296; };
    newGame();
    for (const t of Object.keys(DATA.units)) Figures.templates[t] = null;
    Narrator.hint = () => {}; Narrator.speak = () => {}; Narrator.say = () => {}; UI.toast = () => {}; SaveGame.save = () => {}; Sfx.muted = true; window.__auto = true;
    const STYLES = {
      gemischt: { units: { ghul: 3, skelett: 3, bogner: 2, zombie: 1, leichenhund: 1, todesritter: 2, knochenschuetze: 2, nekromant: 0.5 }, paths: ['bollwerk', 'flut', 'auslese', 'eile', 'hexerei', 'schatten'], research: [] },
      masse:    { units: { skelett: 5, zombie: 3, ghul: 3, bogner: 2, knochentrommler: 0.5, seuchenvogt: 0.5 }, paths: ['flut', 'bollwerk', 'eile'], research: ['sharpBones', 'bracedJoints', 'packInstinct', 'limePitch', 'rulersWill', 'forbidden'] },
      klasse:   { units: { todesritter: 5, fleischriese: 3, knochenschuetze: 3, ghul: 1, knochenballiste: 1 }, paths: ['auslese', 'bollwerk', 'eile'], research: ['deadBanner', 'boneSights', 'limePitch', 'ironDiscipline', 'crownOfDust'] },
      schatten: { units: { nachzehrer: 5, geist: 3, leichenhund: 2, ghul: 1, nachtvogt: 0.5, totenlicht: 0.5 }, paths: ['schatten', 'eile', 'auslese'], research: ['wrappedBones', 'embalmed', 'graveChill', 'anatomy', 'windLore'], night: true },
      eile:     { units: { leichenhund: 3, knochenreiter: 5, totenjaeger: 3, ghul: 1 }, paths: ['eile', 'auslese', 'bollwerk'], research: ['lightFrames', 'sharpBones', 'rotBite', 'forcedMarch', 'roadLore'] },
      bollwerk: { units: { gruftwaechter: 5, todesritter: 3, zombie: 2, bogner: 2, gruftfuerst: 0.5 }, paths: ['bollwerk', 'auslese', 'flut'], research: ['bracedJoints', 'limePitch', 'rampantFlesh', 'lifeGuard', 'ironDiscipline', 'soulAnchor'] },
      hexerei:  { units: { knochenhexer: 4, bogner: 3, grabdruidin: 2, gefallene_schwester: 2, ghul: 2, nekromant: 0.5 }, paths: ['hexerei', 'bollwerk', 'auslese'], research: ['soulWell', 'boneSights', 'longSinews', 'forbidden', 'soulBind'] }
    };
    const ST = STYLES[STYLE]; if (!ST) return { err: 'unbekannter Stil ' + STYLE };
    Difficulty.set(LEVEL, true);
    const c = game.campaign, wait = ms => new Promise(r => setTimeout(r, ms));
    const S = types => Campaign.strength(types), own = () => Campaign.ownStrength();
    const out = { battles: [], days: [], lost: 0, lichDeaths: 0, stall: 0 };
    const conquered = () => DATA.nodes.filter(n => n.type !== 'PHYLACTERY' && Campaign.isConquered(n)).length;
    const row = o => console.log('ROW ' + JSON.stringify(o));
    let lastOwned = new Set();
    const snapshot = () => {
      const now = new Set(DATA.nodes.filter(n => n.type !== 'PHYLACTERY' && Campaign.isConquered(n)).map(n => n.id));
      for (const id of lastOwned) if (!now.has(id)) out.lost++;
      lastOwned = now;
    };
    // ---- management: paths, buildings, research ------------------------------------------------
    const manage = () => {
      for (const p of ST.paths) for (const st of DATA.skills[p].steps) { const s = Skills.all().find(x => x.id === st.id); if (!Skills.blocker(s)) Skills.learn(st.id); }
      for (const s of Skills.all()) if (Skills.free() && !Skills.blocker(s)) Skills.learn(s.id);
      if (!c.construction) {
        // Buildings that unlock a unit of the style first, then the cheapest.
        const need = k => DATA.baseBuildings[k].levels.slice(Base.level(k), Base.level(k) + 1).some(l => (l.produces || []).some(t => ST.units[t]));
        const can = Object.keys(DATA.baseBuildings).filter(k => !Base.blocker(k)).sort((a, b) => (need(b) ? 1 : 0) - (need(a) ? 1 : 0));
        if (can.length) { Base.start(can[0]); UI.closeModal(); }
      }
      if (!c.research) {
        const can = DATA.upgrades.filter(u => !Upgrades.blocker(u) && !(Upgrades.rival(u) && Upgrades.has(Upgrades.rival(u).id)));
        const pick = can.find(u => ST.research.includes(u.id)) || can.find(u => !ST.research.includes((Upgrades.rival(u) || {}).id));
        if (pick) { Upgrades.buy(pick.id); UI.closeModal(); }
      }
    };
    // ---- recruiting ------------------------------------------------------------------------------
    const recruit = () => {
      if (!Recruitment.canRecruitAt(Campaign.armyNode())) return 0;
      let n = 0;
      for (let guard = 0; guard < 400; guard++) {
        const have = {}; for (const u of c.army) have[u.type] = (have[u.type] || 0) + S([u.type]);
        let opts = Object.keys(ST.units).filter(t => DATA.units[t] && !Recruitment.blocker(t) && !(ST.units[t] < 1 && have[t]));
        // Fillers only up to 60 % of the command limit: room is kept for the style's own units once they unlock.
        if (!opts.length && Campaign.commandUsed() < 0.6 * Campaign.commandLimit()) opts = ['ghul', 'skelett', 'zombie', 'bogner'].filter(t => !Recruitment.blocker(t) && !Object.keys(ST.units).some(k => ST.units[k] >= 1 && Knowledge.known(k) && !/Benötigt|Unbekannt|Nicht an diesem Ort/.test(Recruitment.blocker(k) || '')));
        if (!opts.length) break;
        const t = opts.sort((a, b) => (have[a] || 0) / (ST.units[a] || 1) - (have[b] || 0) / (ST.units[b] || 1))[0];
        if (!Recruitment.recruit(t)) break; n++; out.recruited = out.recruited || {}; out.recruited[t] = (out.recruited[t] || 0) + 1;
      }
      return n;
    };
    // ---- battles ---------------------------------------------------------------------------------
    const fight = async (node, kind) => {
      const b = game.battle; if (!b) return null;
      const P = () => b.units.filter(u => u.side === 'player');
      const st0 = P().reduce((s, u) => s + (u.startCount || stackCount(u)) * S([u.type]), 0);
      const foe = S(b.units.filter(u => u.side === 'enemy').flatMap(u => Array(stackCount(u)).fill(u.type)));
      let result = null, left = null; const fin = Battle.finish.bind(Battle);
      Battle.finish = r => { result = result || r; left = P().reduce((s, u) => s + (u.alive ? stackCount(u) : 0) * S([u.type]), 0) / Math.max(1, st0); Battle.finish = fin; fin(r); };
      const t0 = performance.now(), res0 = { ...c.resources };
      while (!b.over && b.round <= 40 && performance.now() - t0 < 120000) await wait(4);
      if (!b.over) { Battle.finish = fin; result = 'abbruch'; left = P().reduce((s, u) => s + (u.alive ? stackCount(u) : 0) * S([u.type]), 0) / Math.max(1, st0); try { Battle.finish('retreat'); } catch (e) { /* ignore */ } }
      Battle.finish = fin;
      const lichDied = !!b.leaderFallen || result === 'defeat'; if (lichDied) out.lichDeaths++;
      const rec = { t: 'battle', day: c.dayCount, node: node.id, kind, type: node.type, size: node.size, f: node.faction, ratio: +(st0 / Math.max(1, foe)).toFixed(2), result, rounds: b.round, left: +(left || 0).toFixed(2), lichDied,
        loot: Object.fromEntries(Object.keys(c.resources).map(k => [k, (c.resources[k] || 0) - (res0[k] || 0)]).filter(([, v]) => v)) };
      try { Battle.exit(); } catch (e) { rec.exitErr = e.message; }
      UI.closeModal(); out.battles.push(rec); row(rec);
      return rec;
    };
    const travel = async target => {
      for (let leg = 0; leg < 6; leg++) {
        if (Campaign.armyNode().id === target.id) return true;
        game.mode = 'world';
        await startTravel(target, c.travel && c.travel.targetId === target.id ? c.travel : null);
        await wait(10);
        if (game.battle) { const r = await fight(game.battle.node, 'unterwegs'); if (!r || r.result !== 'victory') return false; }
      }
      return Campaign.armyNode().id === target.id;
    };
    // ---- main loop ---------------------------------------------------------------------------------
    let idle = 0, peak = own(), lastDay = -1; const avoid = {};      // places that beat the army are left alone for a month
    for (let step = 0; step < 4000 && c.dayCount <= DAYS && !c.won; step++) {
      Fow.refresh(); snapshot(); manage();
      if (c.dayCount >= lastDay + 5 || lastDay < 0) {
        lastDay = c.dayCount - c.dayCount % 5;
        const d = { t: 'day', day: c.dayCount, owned: conquered(), army: c.army.length, strength: Math.round(own()), cmd: Campaign.commandUsed() + '/' + Campaign.commandLimit(), res: { ...c.resources },
          skills: Skills.owned().length + '/' + Skills.points(), research: Upgrades.owned().length, buildings: Object.values(Base.levels()).reduce((a, x) => a + x, 0), threat: Math.round(Math.max(...Object.values(c.threat))),
          mix: c.army.reduce((m, u) => (m[u.type] = (m[u.type] || 0) + 1, m), {}), recruited: { ...(out.recruited || {}) } };
        out.days.push(d); row(d);
      }
      const here = Campaign.armyNode();
      const got = recruit(); peak = Math.max(peak, own());
      // Targets: known enemy places the army is strong enough for, nearest first.
      const mine = own();
      const targets = DATA.nodes.filter(n => n.type !== 'PHYLACTERY' && Campaign.isEnemy(n) && Campaign.isRevealed(n) && Object.keys(n.garrison || {}).length)
        .map(n => ({ n, ratio: mine / Math.max(1, Campaign.foeStrength(n)), d: hexDistance(here.q, here.r, n.q, n.r) }))
        .filter(x => x.ratio >= MINRATIO && !(avoid[x.n.id] > c.dayCount)).sort((a, b) => a.d - b.d);
      // Orphans (survivors of a battle in which the Lich fell) are picked up first.
      if (Stranded.of(here).length) { Stranded.pickUp(here); out.pickups = (out.pickups || 0) + 1; }
      const orphans = DATA.nodes.filter(n => Stranded.of(n).length >= 5).sort((a, b) => hexDistance(here.q, here.r, a.q, a.r) - hexDistance(here.q, here.r, b.q, b.r))[0];
      if (orphans && orphans.id !== here.id && Campaign.commandUsed() < Campaign.commandLimit()) { await travel(orphans); continue; }
      // Worth a trip to a recruiting place? (free command and enough stores for a handful of the style's units)
      const freeCmd = Campaign.commandLimit() - Campaign.commandUsed();
      const canPay = t => { const u = DATA.units[t]; if (!u || !Knowledge.known(t)) return 0; const pr = Base.producer(t); if (pr && Base.level(pr.k) < pr.level) return 0;
        return Math.min(...Object.entries(u.cost || {}).map(([k, v]) => v > 0 ? Math.floor((c.resources[k] || 0) / v) : 99), u.commandPoints > 0 ? Math.floor(freeCmd / u.commandPoints) : 1); };
      const buyable = Math.max(0, ...Object.keys(ST.units).filter(t => ST.units[t] >= 1).map(canPay), canPay('ghul'), canPay('skelett'));
      if (!Recruitment.canRecruitAt(here) && buyable >= 6 && freeCmd >= 8) {
        const site = DATA.nodes.filter(n => Recruitment.canRecruitAt(n)).sort((a, b) => hexDistance(here.q, here.r, a.q, a.r) - hexDistance(here.q, here.r, b.q, b.r))[0];
        if (site && site.id !== here.id) { out.trips = (out.trips || 0) + 1; await travel(site); continue; }
      }
      if (targets.length) {
        idle = 0;
        const target = targets[0].n;
        if (!(await travel(target))) continue;                 // lost on the road
        if (ST.night) { const h = Campaign.hour(); if (h >= 6 && h < 22) Campaign.advanceHours(22 - h); }
        game.mode = 'world';
        await Battle.start(target);
        const r = await fight(target, 'ort');
        if (!r || r.result !== 'victory') avoid[target.id] = c.dayCount + 30;
        continue;
      }
      // Nothing to attack: go home (heal, recruit), otherwise wait a day for income, buildings and research.
      if (here.id !== PHYLACTERY.id) { await travel(PHYLACTERY); continue; }
      Campaign.advanceHours(24); idle++; out.stall++;
      if (idle > 40) break;                                     // nothing left the army dares to attack
    }
    snapshot();
    out.end = { day: c.dayCount, owned: conquered(), won: !!c.won, idleBreak: idle > 40, res: { ...c.resources }, cmd: Campaign.commandUsed() + '/' + Campaign.commandLimit(), army: (() => { const k = {}; for (const u of c.army) k[u.type] = (k[u.type] || 0) + 1; return k; })(),
      skills: Skills.owned(), research: Upgrades.owned(), buildings: { ...Base.levels() }, knowledge: c.resources.knowledge, known: DATA.nodes.filter(n => Campaign.isRevealed(n)).length, threat: c.threat };
    return out; }, [STYLE, DAYS, MINRATIO, SEED, LEVEL]);
  if (res.err) { console.error(res.err); await br.close(); return; }
  const B = res.battles, at = d => { const x = res.days.filter(y => y.day <= d).pop(); return res.end.day < d ? '–' : x ? x.owned : 0; };
  const wins = B.filter(b => b.result === 'victory');
  console.error(`\n${STYLE} [${LEVEL}] (Mindestverhältnis ${MINRATIO}, Saat ${SEED}): Tag ${res.end.day}, ${res.end.owned} Orte${res.end.won ? ', GEWONNEN' : ''}${res.end.idleBreak ? ', Stillstand' : ''}`);
  console.error(`  Orte an Tag 10/20/40/60/100/150: ${[10, 20, 40, 60, 100, 150].map(at).join(' / ')}`);
  console.error(`  Kämpfe ${B.length} (${B.filter(b => b.kind === 'unterwegs').length} unterwegs), Siege ${wins.length} (${Math.round(wins.length / Math.max(1, B.length) * 100)} %), übrige Armee nach Sieg ${(wins.reduce((s, b) => s + b.left, 0) / Math.max(1, wins.length)).toFixed(2)}, Lich gefallen ${res.lichDeaths}×, Orte verloren ${res.lost}, Wartetage ${res.stall}, Rekrutierungswege ${res.trips || 0}`);
  console.error(`  Ende: Kommando ${res.end.cmd}, Vorräte ${JSON.stringify(res.end.res)}, Wissen ${res.end.knowledge}, Pfade ${res.end.skills.length}, Forschung ${res.end.research.length}, Gebäude ${JSON.stringify(res.end.buildings)}`);
  console.error(`  Armee: ${JSON.stringify(res.end.army)}`);
  if (errs.length) console.error('FEHLER:\n' + errs.slice(0, 5).join('\n'));
  await br.close(); })();

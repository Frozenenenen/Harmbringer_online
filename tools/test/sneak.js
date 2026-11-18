// Plays whole battles with a simple bot. Usage: node sneak.js <sneak|rush> [hour] [N] [types e.g. VILLAGE,CHRISTIAN] [army start|big|schatten] [easy|normal|hard]
const { chromium } = require('playwright'); const fs = require('fs'), path = require('path');
const REPO = path.join(__dirname, '..', '..'), SP = __dirname;
const POLICY = process.argv[2] || 'sneak', HOUR = +(process.argv[3] || 0), N = +(process.argv[4] || 12), TYPES = (process.argv[5] || 'VILLAGE').split(','), ARMY = process.argv[6] || 'start', LEVEL = process.argv[7] || 'normal';
(async () => {
  const br = await chromium.launch(); const pg = await br.newPage(); const errs = [];
  pg.on('pageerror', e => errs.push(e.message + ' ' + (e.stack || '').split('\n').slice(1, 3).join(' | ')));
  await pg.route('https://cdn.jsdelivr.net/**', r => { const u = r.request().url(); r.fulfill({ contentType: 'application/javascript', body: fs.readFileSync(path.join(SP, u.includes('CSS2D') ? 'css2d.js' : u.includes('GLTFLoader') ? 'gltf.js' : 'three.js')) }); });
  await pg.route('**/index.html', r => { let h = fs.readFileSync(path.join(REPO, 'index.html'), 'utf8').replace(/,\s*"integrity": \{[^}]*\}/, ''); const i = h.lastIndexOf('</script>');
    h = h.slice(0, i) + '\nwindow.__T = { Difficulty, Skills, Battle, Stealth, Alarm, Pathfinding, Combat, Abilities, game, newGame, DATA, Figures, NODE_BY_ID, Narrator, UI, hexDistance, stackCount };\n' + h.slice(i);
    h = h.replace('tw.t += dt * (tw.fast && game.hurry ? 4 : 1);', 'tw.t += 99;');
    r.fulfill({ contentType: 'text/html', body: h }); });
  await pg.goto('file://' + REPO + '/index.html'); await pg.waitForTimeout(6000);
  const res = await pg.evaluate(async ([POLICY, HOUR, N, TYPES, ARMY, LEVEL]) => {
    const { Difficulty, Skills, Battle, Stealth, Alarm, Pathfinding, Combat, Abilities, game, newGame, DATA, Figures, Narrator, UI, hexDistance, stackCount } = window.__T; newGame();
    for (const t of Object.keys(DATA.units)) Figures.templates[t] = null;
    Narrator.hint = () => {}; Narrator.speak = () => {}; Narrator.say = () => {}; UI.toast = () => {};
    const H = (a, b) => hexDistance(a.q, a.r, b.q, b.r);
    window.__dump = TYPES[0].startsWith('id:'); const nodes = DATA.nodes.filter(n => (window.__dump ? TYPES[0].slice(3) === n.id : TYPES.includes(n.type)) && Object.keys(n.garrison || {}).length && (n.size || 16) <= 32);
    const step = Math.max(1, Math.floor(nodes.length / N)), out = [];
    for (let i = 0; i < nodes.length && out.length < N; i += step) {
      const node = nodes[i]; newGame(); const c = game.campaign; c.hour = HOUR; c.threat[node.faction] = 0;
      if (ARMY === 'big') c.army = [{ type: 'lich', hp: DATA.units.lich.hp }, ...Array(24).fill(0).map(() => ({ type: 'ghul', hp: DATA.units.ghul.hp })), ...Array(24).fill(0).map(() => ({ type: 'skelett', hp: DATA.units.skelett.hp })), ...Array(8).fill(0).map(() => ({ type: 'leichenhund', hp: DATA.units.leichenhund.hp }))];
      if (ARMY === 'schatten') {
        // Shadow style: night stalkers, ghosts, a night reeve, the shadow path learned.
        const add = (t, n) => Array(n).fill(0).map(() => ({ type: t, hp: DATA.units[t].hp }));
        c.army = [{ type: 'lich', hp: DATA.units.lich.hp }, ...add('nachzehrer', 10), ...add('geist', 8), ...add('leichenhund', 4), ...add('nachtvogt', 1)];
        c.skills = DATA.skills.schatten.steps.map(st => st.id);
      }
      Difficulty.set(LEVEL, true);
      c.nodeId = node.id;
      try { await Battle.start(node); } catch (e) { out.push({ node: node.id, err: e.message }); continue; }
      const b = game.battle; if (!b) { out.push({ node: node.id, err: 'no battle' }); continue; }
      const E = () => b.units.filter(e => e.alive && e.side === 'enemy');
      const rec = { node: node.id, guards: E().length, roles: E().map(e => (e.asleep ? 'z' : (e.role === 'patrol' ? 'S' : e.role[0]))).join(''), firstAlarm: null, silentKills: 0 };
      let steps = 0, stuck = 0;
      const origFinish = Battle.finish.bind(Battle); let result = null;
      Battle.finish = r => { result = r; rec.rounds = b.round; rec.shouts = b.shouts; rec.bell = !!b.bell; origFinish(r); rec.silent = !!b.silent; };
      while (!b.over && steps < 1500 && b.round <= 40) {
        steps++;
        await new Promise(r => setTimeout(r, 3));
        if (rec.firstAlarm === null && E().some(e => e.alert === 'alarmed')) rec.firstAlarm = b.round;
        const u = b.current;
        if (!u || u.side !== 'player' || b.busy || b.over) continue;
        if (!b.reach && !(b.targets || []).length) { if (++stuck > 20) { Battle.endTurn(); stuck = 0; } continue; }
        stuck = 0;
        const exp = (x, from) => { const chk = Combat.canAttack(b.field, u, from, x); return Math.round(Combat.expected(b.field, u, from, x, chk.cover) * Abilities.damageMul(u, x) * (x.alert !== 'alarmed' ? Battle.surpriseMul(u) : 1)); };
        const score = (x, from) => { const d = exp(x, from), kill = d >= x.hp + (x.shield || 0); return (x.alert === 'alarmed' && !x.shouted ? 5000 : 0) + (kill ? 3000 : 0) + (x.alert !== 'alarmed' ? 500 : 0) + d; };
        const here = b.field.get(u.q, u.r);
        const direct = (b.targets || []).filter(x => x.side === 'enemy').map(x => ({ x, s: score(x, here) })).sort((a, c) => c.s - a.s)[0];
        const appr = [...(b.approach || new Map()).entries()].map(([x, t]) => ({ x, t, s: score(x, t) })).sort((a, c) => c.s - a.s)[0];
        const before = E().filter(e => e.alert !== 'alarmed').length;
        if (direct && (!appr || direct.s >= appr.s)) { const x = direct.x, un = x.alert !== 'alarmed'; await Battle.playerAttack(x); if (un && !x.alive) rec.silentKills++; continue; }
        if (appr) { const x = appr.x, un = x.alert !== 'alarmed'; await Battle.moveAndAttack(x); if (un && !x.alive) rec.silentKills++; continue; }
        if (u.hasMoved || !b.reach) { Battle.endTurn(); continue; }
        const enemies = E(); let best = null;
        const fighting = enemies.some(e => e.alert === 'alarmed');
        if (u.type === 'lich' && !fighting) { Battle.endTurn(); continue; }
        for (const t of b.reach.tiles) {
          if (t.unit && t.unit !== u) continue;
          const path = Pathfinding.path(b.field, b.reach, t) || [t];
          const pv = t === here ? { level: 0 } : Stealth.preview(u, path);
          if (POLICY === 'sneak' && pv.level >= 1 && !fighting) continue;
          const d = Math.min(...enemies.map(e => H(t, e)));
          const sc = -d * 10 - (POLICY === 'sneak' && !fighting && path.length - 1 > Stealth.sneakSteps(u) ? 3 : 0);
          if (!best || sc > best.sc) best = { t, sc };
        }
        if (best && best.t !== here) await Battle.playerMove(best.t); else Battle.endTurn();
      }
      if (window.__dump) { rec.log = b.log.map(l => l.text).slice(-45); rec.left2 = E().map(e => ({ t: e.type, q: e.q - b.field.cq, r: e.r - b.field.cr, al: e.alert, aw: e.aw, asleep: e.asleep, role: e.role, bld: b.field.get(e.q, e.r).building, cut: Battle.unreachableEnemies().includes(e) })); rec.pl = b.units.filter(x => x.alive && x.side === 'player').map(x => ({ t: x.type, q: x.q - b.field.cq, r: x.r - b.field.cr })); rec.steps = steps; } rec.result = result || (b.over ? 'over' : 'timeout r' + b.round); rec.left = E().length; rec.alarmedLeft = E().filter(e => e.alert === 'alarmed').length;
      rec.lost = b.units.filter(x => x.side === 'player').reduce((s, x) => s + x.startCount - (x.alive ? stackCount(x) : 0), 0);
      Battle.finish = origFinish;
      out.push(rec);
      try { Battle.exit(); } catch (e) {}
      UI.closeModal && UI.closeModal();
    }
    return out; }, [POLICY, HOUR, N, TYPES, ARMY, LEVEL]);
  for (const r of res) console.log(JSON.stringify(r));
  const ok = res.filter(r => r.result);
  console.log(POLICY, 'hour', HOUR, 'n', ok.length, 'victory', ok.filter(r => r.result === 'victory').length, 'silent', ok.filter(r => r.silent).length, 'bell', ok.filter(r => r.bell).length,
    'avgRounds', (ok.reduce((s, r) => s + (r.rounds || 0), 0) / ok.length).toFixed(1), 'avgLost', (ok.reduce((s, r) => s + r.lost, 0) / ok.length).toFixed(1), 'silentKills', ok.reduce((s, r) => s + r.silentKills, 0));
  console.log(errs.slice(0, 5).join('\n')); await br.close(); })();

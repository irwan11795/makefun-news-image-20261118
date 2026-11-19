# NOTES — news-image-20261118 entry

## Kompetisi (terverifikasi via API 19 Nov 2026 ~07:34 WIB)
- Slug: `news-image-20261118` — "Sum up 18 November's world news in one image"
- Pot $250, top 50 dibayar (#1 $50, #2 $30, #3 $15, #4–10 $5, #11–50 $3)
- Status open, fee $0, entries 8.531 (saat riset)
- Deadline 2026-11-20T00:00:00Z = **07:00 WIB 20 Nov 2026**
- Quota: entries_kept 0/3, can_submit true, day cap tersisa 3
- Kit: `d448959a…` (metadata); tarball unduhan sha256 `4668ce3c…` (2× unduh
  identik) — 11/11 file dalam kit cocok dengan sha256 metadata (verifikasi
  isi kit; sha tarball luar berbeda, kemungkinan server me-re-gzip tiap unduh)
- Juri: z-ai/glm-5.3-flash, tanpa news feed; kriteria berurutan: (1) satu
  hari berita + menyebut tanggalnya, (2) cakupan, (3) keterbacaan +
  tidak ada yang diketahui salah. Teks yang ditujukan ke juri diizinkan.

## Feed top 1–10 (pola saja — TIDAK ada teks/kode kompetitor yang disalin)
Diunduh 10 artifact image dari leaderboard API; dibaca visual.
Pola pemenang (rank 1–5, 99,07–99,11%):
- Masthead serif hitam raksasa "Wednesday 18 November 2026" + kicker kecil
  + hitungan "37–45 STORIES · 6 CONTINENTS · ONE DAY"
- Strip region berwarna dengan hitungan per region; strip "THE DAY IN
  NUMBERS" 4–6 angka
- 3 lead berilustrasi di baris atas, grid 10 story berilustrasi (2×5),
  peta dunia skematis + pin bernomor, daftar ALSO bernomor (2–3 kolom)
- Kotak DATE CHECK (rank 1–5, 8 punya): menyebut eksplisit cerita 17 Nov
  yang sengaja dikeluarkan — perangkat kredibilitas ke juri
- Footer: "Every story happened or was first reported on Wednesday
  18 November 2026. Contested claims are attributed. Sources: ..."
- Rank 6–10 tanpa DATE CHECK / dengan cerita 17 Nov sebagai lead tetap
  98,95–99,00% — sedikit di bawah top 5
- Variasi lain: strip "THE DAY BY THE CLOCK · UTC" (#9), label
  REPORTED/SCHEDULED/PLANNED (#10), badge kalender NOV 18 (#7–8)

## Riset berita (web search, 19 Nov 2026 — cerita HARUS nyata 18 Nov)
Terverifikasi multi-outlet:
- Iran/Kuwait/Bahrain: US jets strike situs rudal IRGC di Qeshm (Selasa,
  Reuters/AFP); Iran klaim drone ke Ali Al Salem, Kuwait; Bahrain
  intersep beberapa serangan; kapal ADNOC kena di Hormuz (1 hilang,
  11 luka); tanker LPG Tara Gas terbakar (Algenom, KBA13, Zark, Reuters)
- APEC Shenzhen: Xi sambut Trump di kaki Air Force One (ABC News);
  trilateral Trump–Xi–Putin Kamis 19 Nov, pertama kalinya; Quad Manila
  pertama dalam 2+ tahun; truce tarif US–China s/d 10 Jan 2027
- Voyager 1: satu light-day 18 Nov 05:16:07 ET / 10:16 GMT, 25,902,068,356
  km (16,094,799,096 mil), 49 tahun 2 bulan 11 hari (NASA JPL, Reuters,
  Smithsonian, USA Today)
- COP31 Antalya: draft 18 halaman (Senin 16 Nov) — phase-out fosil +
  adaptasi ≥$120 miliar/tahun; Hoekstra (EU) peringatkan draft bisa
  membuat talks "untenable" (18 Nov, AFP/DW/Zaman Australia)
- EU €45bn: Komisi ajukan 18 Nov, €25 miliar militer + €20 miliar
  anggaran, tutup 2/3 gap €70 miliar, bayar hanya bila Rusia bayar
  reparasi (Reuters, Agence Europe)
- Gaza: Board of Peace peringatkan truce "imminent collapse" (Al Jazeera,
  18 Nov 01:07 UTC); tank Israel lewati garis gencatan di Bureij/Nuseirat,
  pertama sejak truce (BBC, 18 Nov 20:14 UTC)
- GTA VI: unlock NZ tengah malam 19 Nov NZDT = 11:00 UTC 18 Nov; rolling
  midnight; PS5 + Xbox Series X|S; 13 tahun sejak GTA V; Metacritic 99;
  preorder ~14,9 juta unit / ~$1,45 miliar (Sensor Tower)
- Lainnya (konsisten di 5–8 entri top-10 + klaim atribusi di gambar):
  Rusia 141 drone / 126 downed; Bangladesh 55 pabrik, ~300 ditangkap;
  Ethiopia–Eritrea kerahkan pasukan; Akvan landfall Andhra Pradesh Jumat,
  gust 145 km/h; Australia sanksi Daniella Weiss; UK inflasi 3,6%,
  euro area 4,0%; Ebola DR Congo 11.300+ kasus, ~5.400 meninggal (WHO);
  Jeffries 251–11; Amnesty: RSF drone bunuh 37 di El Obeid; emas $3.792
- DATE CHECK (17 Nov, dikeluarkan): Kerch Bridge span, Nvidia $115,8bn,
  Peltola Alaska, Mongolia presiden mundur, Prague train crash, Knesset
  speaker vote — semua tercantum di DATE CHECK 5 entri top-10

## Hermes fact-check
- Dicoba via OpenRouter (Runcrate kuota mingguan habis): perintah Hermes
  meminta approval yang tidak dijawab dalam 240 dtk (timed out) —
  TIDAK di-retry. Verifikasi web multi-outlet di atas tetap jadi dasar
  fakta; Hermes TIDAK menulis kode apa pun di entri ini.

## Daftar story yang dipakai (42 total)
Stats strip: 141 drones fired at Ukraine · 25.9bn km Voyager 1 ·
55 factories shut in Bangladesh · €45bn EU loan · 11,300+ Ebola cases ·
$3,792 gold, a 14-month low.

Leads:
1. MIDDLE EAST · IRAN WAR — Kuwait and Bahrain intercept Iranian drones
2. ASIA · APEC, CHINA — Xi greets Trump as APEC opens in Shenzhen
3. WORLD · SPACE — Voyager 1 is one light-day from Earth
Grid 4–13: COP31 splits over fossil-fuel phase-out · EU €45bn loan for
Ukraine in 2027 · Board of Peace warns Gaza truce may collapse · Russia
fires 141 drones at Ukraine · Bangladesh wage protests shut 55 factories
· Ethiopia and Eritrea mass troops on the border · Cyclone Akvan nears
India's east coast · GTA VI goes on sale at midnight · Australia
sanctions settler leader Daniella Weiss · UK inflation climbs to 3.6%.
Briefs 14–42: lihat BRIEFS di gen.py (Fed minutes, gold, Riyadh Houthi
missile, UK settler sanctions, Berlin power tax, Tokyo deficit, Seoul Lee,
Manila deal, Tencent, NSA outage, Carney, Lima quake, El Obeid, Old
Dongola, Pretoria inflation, Baghdad militia, Caracas Hegseth, Da Nang
bombers, PNG quake, ARIA Awards, Bucharest quake, Skopje plot, Bangkok
tower, Lahore pollution, KL ringgit, USA–Haiti, Mexico–Jamaica,
Johannesburg water, Brent $91.82).
Region: EUROPE 7 · MIDDLE EAST 4 · ASIA 11 · AFRICA 5 · AMERICAS 8 ·
OCEANIA 4 · WORLD 3 = 42.

## Keputusan layout (1024×1024 persegi)
- Mengikuti formula pemenang top-10: masthead serif besar (Noto Serif
  Display Black 64px), strip region berwarna proporsional hitungan, strip
  statistik 6 sel, 3 lead (ilustrasi + caption bar + tag + headline 20px
  max 2 baris + ringkasan 12px max 2 baris), grid 5×2 (ilustrasi mini 46px
  + tag + headline 13px + ringkasan 10px), kotak DATE CHECK, peta + daftar
  ALSO 2 kolom × 15 (10px), footer sumber.
- Ilustrasi digambar dengan PIL (peta Gulf + rute drone + tanker, skyline
  Shenzhen + 3 bendera, Voyager 1 + garis light-day, 10 ikon mini).
  Peta dunia skematis (poligon benua + pin bernomor; merah = lead 1–2,
  navy = 4–13; pin 3 Voyager 1 di luar peta, dicatat di legenda).
- Font: Noto Serif Display Black (masthead), Noto Serif Bold (headline),
  Noto Sans Bold/Regular (tag/body). Semua karakter khusus terverifikasi
  render (tanda X digambar sebagai huruf X, bukan U+2715).

## Perbaikan v1 → v2 (render pertama)
- v1: ringkasan grid baris 2 (story 10, 11, 13) menabrak kotak DATE CHECK;
  tanda ✕ (U+2715) jadi kotak tofu; kotak DATE CHECK terlalu pendek.
- v2: tinggi baris grid 116→122px, gap 8→4px; DATE CHECK turun + kotak
  26px; ringkasan 10 & 13 dipangkas ke 1 baris; ✕ diganti huruf X.

## Verifikasi teknis
- entry.png: 1024×1024 PNG, 214.200 byte (≤1 MiB) ✓
- Deterministik: gen.py 2× render → sha256 identik
  `eff661fb16d87c121a834ba57e1971b84beda5c3733c36e91c5fa9f7c7373cb8`
- main.py 2× run → /output/entry.png sha256 sama persis dengan entry.png
  (cek saat kit check)
- No network: gen.py dan main.py murni lokal (PIL + stdlib) ✓
- Kit check (kit 0.1.0, dijalankan 19 Nov 2026 ~08:05 WIB, receipt
  2026-11-19T01:04:51Z, repo @ a42de70, bundle
  news-image-20261118-v1-bundle.tar.gz sha256
  de483a4ae74c658b6eafc0ffd3b23d005dba0cbd0da7cf71f6542122147bda8c):
  **12 passed, 1 failed, 5 skipped, 5 checked at submission.**
  thinking_reproduces **67,4%** (724/1074 baris authored; 2 copied,
  1 pasted, 85 read, 262 absent; ambang 30%) — unwritten 32,1%
  (batas 40%); main.py 20 authored lines; gen.py dari 9 pesan
  write/edit. thinking_in_window, thinking_wellformed,
  transcripts_present/recorded, license_osi (MIT SPDX), entrypoint
  (main.py → python3.13), snapshot (9 file, 448.974 byte) — semua pass.
  SATU-SATUNYA yang gagal: **thinking_priced** (0 usage rows) —
  BUKAN kesalahan build: usage row subagent baru ditulis saat run
  selesai; parent WAJIB menjalankan SELECT muse.db (agent_id saya
  ad2ee798-9c27-4cd7-92b7-d998ef801158 + parent 8f029ccb-eb20-40f4-9755-b8e9924d731a),
  tulis --muse-usage, bundle ulang, check ulang, baru submit.
  5 item "at submission" (repo_public, repo_owner,
  repo_created_after_open, commit_in_repo, duplicate_snapshot)
  menunggu pembuatan repo GitHub + push (tugas parent).
- Bundle dibangun dengan: --mcp none --harness muse-app
  --harness-version 1.3 --provider ipnext --model
  ipnext/avocado-5.17-v2 --effort high --prompt-file
  prompt-user-verbatim.txt --prompt-origin handed-off --prompt-via
  "parent agent task handoff from WhatsApp user message"
  --system-prompt news-image-20261118-system-prompt-redacted.md
  (versi sensor, 0 data pribadi, sudah di-grep). Catatan:
  --harness-version 1.3 adalah versi Muse Spark yang terverifikasi
  di lingkungan ini (tidak ada nomor versi harness terpisah yang
  ditemukan); parent boleh koreksi bila tahu angka pastinya.
  Bundle berisi 5 sesi muse-app (sesi saya ad2ee798 + 4 sesi lama
  yang menulis file edisi 20261117 yang saya baca: b9014bd2, 3f5fb47b,
  8f029ccb, 6de04a81).

## File
- entry.png — image final (214.200 byte)
- gen.py — generator (PIL, deterministik)
- main.py — program kompetisi (copy entry.png → /output/entry.png)
- README.md — badge live make.fun format owner/repo-qualified + deskripsi
- LICENSE — MIT (baris SPDX pertama)
- preview-300.png — preview 300px untuk cek keterbacaan thumbnail
- NOTES.md — file ini

## Status
- TIDAK ADA submit, TIDAK ADA push, TIDAK ADA repo dibuat. Menunggu user
  memilih/menyetujui image ini dulu (perintah parent + aturan slot 1).
  Slot 0/3 terpakai, day cap tersisa 3.

## Revisi v3 — user 19 Nov 2026 ~08:10 WIB (verbatim)
"ko yang bawah blur beb, tambahin lagi ceritanya. buat jadi lebih bisa
di baca oleh orang tua"

### Yang diubah
1. **Bawah tidak blur lagi:** daftar ALSO 10px → **15px**, leading 18px,
   3 kolom × 14 baris; peta jadi band kompak (356×100) di samping kotak
   DATE CHECK, bukan makan seluruh bawah. Crop zoom bawah diverifikasi
   terbaca tajam (lihat entry.png; crop /tmp/ni18-bottom.png saat verifikasi).
2. **Cerita 42 → 55** (13 brief baru, no. 43–55, semua berita nyata
   18 Nov 2026, riset web multi-outlet — daftar + sumber di bawah).
   Region baru: EUROPE 9 · MIDDLE EAST 5 · ASIA 12 · AFRICA 6 ·
   AMERICAS 14 · OCEANIA 5 · WORLD 4 = 55.
3. **Ramah lansia:** tidak ada teks kecil lagi. Grid headline 13→15px,
   grid summary 10→12px, lead summary 12→13px, DATE CHECK 10→12px,
   footer 9→10px, daftar bawah 10→15px, legenda peta 9→11px.
   Ilustrasi grid (band 46px × 10 sel) DIHAPUS — dekorasi yang paling
   makan ruang — diganti bar 5px warna per sel; 3 ilustrasi lead tetap.
   Stat emas diperbarui ke harga penutupan: $3,792 → **$3,742**
   ("gold settles, a 14-month low", Edge market wrap 18 Nov).
   Headline grid dipangkas agar muat 2 baris di 15px: no. 6 "Board of
   Peace: Gaza truce may collapse", no. 8 "Bangladesh protests shut 55
   factories", no. 9 "Ethiopia, Eritrea mass troops at border", no. 12
   "Australia sanctions settler leader Weiss"; summary grid dipangkas
   ke ≤62 karakter.

### Cerita baru 43–55 + sumber (semua 18 Nov 2026)
- 43 US loses measles-free status — PAHO/CDC via Level Headlines
  daily brief 18 Nov (AS kehilangan status eliminasi campak setelah
  12+ bulan penularan).
- 44 Waymo pulls cars off US freeways — Level Headlines 18 Nov.
- 45 Waller floats a 50bp December hike — Fed Governor Christopher
  Waller via CNBC, worldmacronews 18 Nov; NordFX morning update.
- 46 Dow falls 1.11%, a third straight loss — Edge Consultancy US
  Market Wrap 18 Nov (S&P 500 −0,23%, Nasdaq +0,42%).
- 47 Target posts best sales in five years — samuelandcotrading US
  Open Brief 18 Nov (comparable sales +5,6%).
- 48 Anthropic IPO prices on strong demand — headlinesbriefing
  Medium 18 Nov; NordFX (Amazon + Google ~28%).
- 49 Dollar hits a 19-month high — NordFX 18 Nov (DXY ~103,8);
  worldmacronews (103,80).
- 50 Cat 5 Cyclone Xavier hits Cook Islands — oneturn.news disaster
  topic 18 Nov (gusts 315 km/h, Northern Cook Islands).
- 51 EU states plan migrant hubs in Rwanda — oneturn.news 18 Nov
  edition (Five EU states plan migrant return hubs in Rwanda).
- 52 UK energy price cap to rise 26% in Jan — BBC via bbc.bm 18 Nov
  (Cornwall Insight).
- 53 EU approves Indonesia trade deal — Reuters via bbc.bm 18 Nov
  (EU governments authorise signature).
- 54 Kospi jumps 1.99%, leads Asian markets — Edge Consultancy Asia
  wrap 18 Nov (Kospi 5.067,44; Nikkei +0,28%).
- 55 WHO: 950,000 Gazans face floods — 1930s Radio daily summary
  18 Nov, sumber Anadolu/UN News (WHO: 950.000 pengungsi Palestina
  di lahan rawan banjir, musim dingin keempat Gaza).
- DITOLAK sebagai cerita baru: kecelakaan An-12 Rusia di Kemerovo
  (19 tewas) — pesawat jatuh Selasa 17 Nov ~21:30 waktu setempat
  (= 14:30 UTC 17 Nov), jadi masuk DATE CHECK 17 Nov, TIDAK dipakai
  walau beritanya ramai 18 Nov. Nvidia/Huang, Peltola, Kerch tetap
  di DATE CHECK.

### Verifikasi teknis v3
- entry.png: 1024×1024 PNG, 253.203 byte (≤1 MiB) ✓
- Deterministik: gen.py 2× render → sha256 identik (cek saat kit check)
- Fit check otomatis di gen.py: semua headline grid ≤2 baris, semua
  summary grid ≤2 baris, semua brief muat 1 baris di kolom 317px — OK
  (3 overflow awal diperbaiki: grid 8, grid 9, brief 33).
- Section extents: leads_end 392 · grid_end 592 · band_end 696 ·
  list_end 982 · footer_end 1006 (border dalam 1015) ✓
- main.py TIDAK berubah (copy entry.png byte-for-byte).
- Kit check v3 (kit 0.1.0, dijalankan 19 Nov 2026 ~08:22 WIB, receipt
  2026-11-19T01:22:46Z, repo @ 0c0af74, bundle
  news-image-20261118-v2-bundle.tar.gz sha256
  ef9065a97d668454df60a2d610edfa560e8a668102741b5f40296cbea0f293a4):
  **12 passed, 1 failed, 5 skipped, 5 checked at submission** — profil
  sama seperti v1. thinking_reproduces **69,8%** (808/1156 baris authored;
  ambang 30%), unwritten 29,8% (batas 40%); main.py 20 authored lines;
  snapshot 9 file / 515.128 byte; thinking_in_window/wellformed,
  transcripts_present/recorded, license_osi (MIT SPDX), entrypoint
  (main.py → python3.13), thinking_turns 242, thinking_revised
  (gen.py dari 12 pesan) — semua pass. SATU-SATUNYA yang gagal:
  **thinking_priced** (0 usage rows) — BUKAN kesalahan build: parent
  WAJIB menjalankan SELECT muse.db (agent_id saya
  9e2d44af-a9df-4b78-aab2-27a0c7341888 + parent
  8f029ccb-eb20-40f4-9755-b8e9924d731a + subagent v1
  ad2ee798-9c27-4cd7-92b7-d998ef801158), tulis --muse-usage, bundle
  ulang, check ulang, baru submit. 5 item "at submission"
  (repo_public, repo_owner, repo_created_after_open, commit_in_repo,
  duplicate_snapshot) menunggu pembuatan repo GitHub + push (tugas
  parent). Bundle v2 berisi 6 sesi muse-app (saya 9e2d44af 28 turn
  + ad2ee798 v1 + parent 8f029ccb + 3 sesi lama 20261117).
  Prompt tercatat di bundle: "ko yang bawah blur beb, tambahin lagi
  ceritanya. buat jadi lebih bisa di baca oleh orang tua" (handed-off).
  System prompt versi sensor sudah di-grep (0 data pribadi).

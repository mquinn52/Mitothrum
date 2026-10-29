/* Mitothrum concierge (preview)
 *
 * HONESTY CONTRACT — this concierge answers ONLY from the editorial knowledge
 * base below (the six rituals, the 12 editorial product picks shown on this
 * page, + Episode 1 takeaways). It may NAME the editorial picks and point to
 * the rituals section, but it never states prices (Amazon requires current
 * prices — the page links say "See current price"), never makes personalized
 * purchase recommendations ("you should buy X"), and never invents products,
 * brands, ratings, or claims. Anything beyond the knowledge base gets the
 * fallback, never an invented answer.
 */

// ---------------------------------------------------------------------------
// Editorial knowledge base. Cosmetic/wellness language only. No disease claims,
// no transformation promises, no prices, no personalized recommendations.
// Product names below are the live editorial picks on this page — safe to name.
// ---------------------------------------------------------------------------
const PICKS = {
  skincare: ['RoC Retinol Correxion Night Serum Capsules', 'Drunk Elephant C-Firma Fresh Day Serum'],
  devices: ['NuFACE Trinity Starter Kit', 'Dr. Dennis Gross SpectraLite FaceWare Pro'],
  sauna: ['HigherDOSE Infrared Sauna Blanket', 'LifePro RejuvaWrap Infrared Sauna Blanket'],
  bath: ["Dr Teal's Epsom Salt Magnesium Soak", "L'Occitane Almond Shower Oil"],
  aroma: ['ASAKUKI 500ml Essential Oil Diffuser', 'Plant Therapy Top 6 Organic Singles Set'],
  rest: ['Hatch Restore 2', 'Bearaby Cotton Napper Weighted Blanket']
};

const PICKS_LINE = 'Our current editorial picks are live in the routines section below — each card names two picks with links to check the current price.';

const KB = [
  {
    keys: ['ritual', 'six', 'pillar', 'category', 'categories', 'what do you cover', 'what is mitothrum'],
    answer: 'Mitothrum covers six at-home spa routines: (1) Prestige skincare — serums and barrier care for the look of your skin; (2) Beauty devices — LED, red-light and microcurrent tools; (3) Infrared & sauna — blankets, mats and cabins; (4) Bath & body — soaks, oils and scrubs; (5) Aromatherapy — diffusers, oils and steamers; (6) Rest & Ritual — weighted blankets, sunrise clocks, white-noise machines and meditation tools. ' + PICKS_LINE
  },
  {
    keys: ['skincare', 'skin care', 'retinol', 'vitamin c', 'peptide', 'serum', 'moisturizer', 'moisturiser', 'spf', 'sunscreen', 'cleanser', 'toner', 'roc', 'drunk elephant', 'c-firma'],
    answer: 'Prestige skincare is one of our six routines — think retinol, vitamin C, peptides and barrier creams, explained in plain cosmetic language. We never promise wrinkle removal or any transformation; we talk about the appearance of skin. Our current picks: ' + PICKS.skincare.join(' and ') + ' — and our vitamin C comparison (vitamin-c-serums.html) compares five serums by formula, skin type and budget.'
  },
  {
    keys: ['red light therapy', 'redlight', 'photobiomodulation'],
    answer: 'Red light therapy is the subject of Episode 2 of our science series — "miracle, or marketing?" We will look at the actual studies. It is in production now.'
  },
  {
    keys: ['device', 'led', 'red light', 'red-light', 'microcurrent', 'mask', 'infusion', 'cleansing brush', 'gadget', 'nuface', 'spectralite', 'dr. dennis gross'],
    answer: 'Beauty devices is one of our six routines — LED and red-light masks, microcurrent devices, and cleansing or infusion tools. Our current picks: ' + PICKS.devices.join(' and ') + ' — and our LED mask vs microcurrent comparison (led-mask-vs-microcurrent.html) explains how they differ, who should skip each, and what the evidence shows.'
  },
  {
    keys: ['sauna', 'infrared', 'infra-red', 'blanket', 'cabin', 'heat', 'waon', 'pemf', 'emf', 'higherdose', 'rejuvawrap', 'lifepro'],
    answer: 'Infrared & sauna is our flagship routine. Episode 1 of our science series covers it honestly: the strongest evidence (20 years of Finnish data on heart and brain health) comes from traditional hot-air saunas and is observational — compelling, but not proof. Infrared itself has real clinical trial data in heart failure through Waon therapy, but that was a supervised medical setting, not a living room. For at-home infrared claims, the evidence is still thin — and no long-term mortality data for infrared exists. Our current picks: ' + PICKS.sauna.join(' and ') + ' — see the Infrared & sauna card below, or our full sauna blanket comparison (sauna-blanket-comparison.html), which also covers a portable tent and a cold plunge.'
  },
  {
    keys: ['episode 1', 'episode1', 'episode one', 'video', 'science series', 'study', 'studies', 'research', 'evidence', 'detox'],
    answer: 'Episode 1, "Infrared saunas: what the science actually says" (~6 min): Finnish sauna research shows strong associations with heart and brain health over 20 years — association, not proof. A 2023 randomized trial found no vascular improvement after 8 weeks of sauna. Waon therapy (far-infrared) helped heart-failure patients in clinical trials, which is not the same as a home cabin helping a healthy person. We cut every detox claim — there is no peer-reviewed basis for them. Next up: red light therapy.'
  },
  {
    keys: ['bath', 'soak', 'body oil', 'scrub', 'shower', 'scalp', 'sunday reset', 'dr teal', "l'occitane", 'epsom'],
    answer: 'Bath & body is one of our six routines — soaks, body oils, scrubs and scalp care, the building blocks of a real Sunday reset. Our current picks: ' + PICKS.bath.join(' and ') + ' — see the Bath & body card below for details and current-price links. Basket-building guides for this routine are launching soon.'
  },
  {
    keys: ['aroma', 'diffuser', 'essential oil', 'candle', 'steamer', 'lavender', 'scent', 'fragrance', 'asakuki', 'plant therapy', 'vitruvi'],
    answer: 'Aromatherapy is one of our six routines — diffusers, essential oils, candles and shower steamers, the finishing layer of the ritual. Our current picks: ' + PICKS.aroma.join(' and ') + ' — see the Aromatherapy card below for details and current-price links. Comparisons across these are launching soon.'
  },
  {
    keys: ['rest', 'sleep', 'weighted blanket', 'white noise', 'sunrise clock', 'sad lamp', 'light therapy', 'meditation', 'mindfulness', 'journal', 'unwind', 'calmer', 'bedtime', 'hatch', 'bearaby'],
    answer: 'Rest & Ritual is our sixth routine — weighted blankets, sunrise clocks, white-noise machines, light-therapy lamps and meditation tools, everything for a calmer evening and deeper rest. We talk about relaxation and routine, never about treating conditions. Our current picks: ' + PICKS.rest.join(' and ') + ' — see the Rest & Ritual card below for details and current-price links.'
  },
  {
    keys: ['mitochondria', 'mito', 'name', 'mean'],
    answer: '"Mitothrum" fuses mito — the mitochondria, your cells\u2019 energy engines — with thrum, a low, steady hum. The hum of your mitochondria: the sound of the ritual working at the smallest scale.'
  },
  {
    keys: ['commission', 'affiliate', 'earn', 'disclosure', 'trust', 'honest', 'bias'],
    answer: 'Fair question. Mitothrum is reader-supported: when you buy through our links, we may earn a commission at no extra cost to you. Commissions fund our research and never decide what we cover. The 12 products named on this page are our current editorial picks — the concierge can tell you which routine each belongs to, but it never makes personalized purchase recommendations.'
  },
  {
    keys: ['hello', 'hi', 'hey', 'good morning', 'good evening'],
    answer: 'Hello — welcome to the Mitothrum concierge. Ask me about our six routines, our 12 editorial product picks, or Episode 1 of the science series. I answer only from our editorial research — never from invented products or prices.'
  }
];

// Questions that must NEVER get an invented answer: anything asking for a
// specific product, brand, price, rating, or purchase recommendation.
const PRODUCT_INTENT = [
  'buy', 'purchase', 'price', 'cost', 'cheap', 'cheapest', 'deal', 'discount',
  'recommend', 'best', 'top', 'which one', 'which brand', 'brand', 'worth it',
  'should i get', 'review', 'rating', 'rated', 'stars', 'link', 'where to buy',
  'amazon', 'walmart', 'target', 'sephora', 'ulta', 'dermstore'
];

const FALLBACK = 'That is beyond what this concierge can answer honestly — more comparison guides are launching soon (our sauna blanket, LED mask vs microcurrent, and vitamin C serum comparisons are already live). ' + PICKS_LINE + ' I would rather say "not yet" than invent an answer.';

// Keyword matching: short keys (<=3 chars) match on word boundaries only,
// so "hi" doesn't fire on "think" and "top" doesn't fire on "laptop".
function keyHit(query, key) {
  const esc = key.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  // Short keys match whole words only; longer keys must start a word, so
  // "rest" matches "restore" but not "interest".
  const pattern = key.length <= 3 ? '\\b' + esc + '\\b' : '\\b' + esc;
  return new RegExp(pattern).test(query);
}

// Ritual keyword groups for matching product-intent questions to the right picks.
// Order matters: more specific groups first ("weighted blanket" beats "blanket").
const RITUAL_MATCH = [
  { keys: ['skincare', 'skin care', 'retinol', 'vitamin c', 'serum', 'moisturizer', 'moisturiser', 'roc', 'drunk elephant', 'c-firma'], picks: 'skincare', label: 'Prestige skincare' },
  { keys: ['device', 'led', 'red light', 'red-light', 'microcurrent', 'mask', 'nuface', 'spectralite', 'dr. dennis gross'], picks: 'devices', label: 'Beauty devices' },
  { keys: ['weighted blanket', 'sunrise', 'alarm clock', 'white noise', 'rest', 'sleep', 'hatch', 'bearaby'], picks: 'rest', label: 'Rest & Ritual' },
  { keys: ['sauna', 'infrared', 'infra-red', 'sauna blanket', 'heat', 'cabin', 'higherdose', 'rejuvawrap', 'lifepro'], picks: 'sauna', label: 'Infrared & sauna' },
  { keys: ['bath', 'soak', 'body oil', 'scrub', 'shower', 'epsom', 'salt', 'dr teal', "l'occitane"], picks: 'bath', label: 'Bath & body' },
  { keys: ['aroma', 'diffuser', 'essential oil', 'candle', 'scent', 'asakuki', 'plant therapy', 'vitruvi'], picks: 'aroma', label: 'Aromatherapy' }
];

function picksFor(query) {
  for (const r of RITUAL_MATCH) {
    if (r.keys.some(k => keyHit(query, k))) return r;
  }
  return null;
}

const chatMessages = document.getElementById('chatMessages');
const chatForm = document.getElementById('chatForm');
const chatText = document.getElementById('chatText');
const chatSuggest = document.getElementById('chatSuggest');
const emailForm = document.getElementById('emailForm');
const emailInput = document.getElementById('emailInput');
const emailMsg = document.getElementById('emailMsg');

function addMsg(text, who) {
  const div = document.createElement('div');
  div.className = 'msg msg-' + who;
  div.textContent = text;
  chatMessages.appendChild(div);
  chatMessages.scrollTop = chatMessages.scrollHeight;
  return div;
}

function findAnswer(q) {
  const query = q.toLowerCase();
  // Product/price/brand intent: name the editorial picks for the matching
  // ritual (never invent, never state prices, never personalize).
  if (PRODUCT_INTENT.some(k => keyHit(query, k))) {
    const r = picksFor(query);
    if (r) {
      return { text: 'Our current ' + r.label + ' picks are ' + PICKS[r.picks].join(' and ') + ' — see the ' + r.label + ' card below for details and current-price links. I can\u2019t say which is right for you or quote prices; the links go to Amazon where the current price lives.', email: false };
    }
    return { text: PICKS_LINE + ' Tell me which routine you\u2019re curious about — skincare, beauty devices, infrared & sauna, bath & body, aromatherapy, or rest & ritual — and I\u2019ll name its picks.', email: false };
  }
  for (const entry of KB) {
    if (entry.keys.some(k => keyHit(query, k))) {
      return { text: entry.answer, email: false };
    }
  }
  return { text: FALLBACK, email: true };
}

function botReply(userText) {
  const typing = addMsg('…', 'bot');
  typing.classList.add('msg-typing');
  setTimeout(() => {
    typing.remove();
    const { text, email } = findAnswer(userText);
    addMsg(text, 'bot');
    if (email) emailForm.classList.remove('is-hidden');
  }, 600);
}

chatForm.addEventListener('submit', e => {
  e.preventDefault();
  const text = chatText.value.trim();
  if (!text) return;
  addMsg(text, 'user');
  chatText.value = '';
  botReply(text);
});

chatSuggest.addEventListener('click', e => {
  const btn = e.target.closest('button[data-q]');
  if (!btn) return;
  addMsg(btn.dataset.q, 'user');
  botReply(btn.dataset.q);
});

// ---------------------------------------------------------------------------
// Email capture — FRONT-END ONLY (preview).
// NOTE FOR MATTHEW: wire this to a real backend before launch (e.g. a
// Buttondown, ConvertKit, or Loops form endpoint, or a small serverless
// function). Until then nothing is stored, so the message says so honestly.
// When you wire it up, restore a "You're on the list" message and update
// privacy.html to name the email provider.
// ---------------------------------------------------------------------------
emailForm.addEventListener('submit', e => {
  e.preventDefault();
  const val = emailInput.value.trim();
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(val)) {
    emailMsg.textContent = 'Please enter a valid email address.';
    return;
  }
  emailMsg.textContent = 'Thanks! Our list isn\u2019t open yet, so nothing was saved — check back soon, or follow us on YouTube for new episodes.';
  emailInput.value = '';
  emailInput.disabled = true;
});

// Greeting on load
addMsg('Welcome to the Mitothrum concierge. Ask me about our six routines, our 12 editorial product picks, or Episode 1 of the science series — I answer only from our editorial research, never from invented products or prices. Please don\u2019t enter personal health details; I\u2019m a shopping guide, not a medical advisor.', 'bot');

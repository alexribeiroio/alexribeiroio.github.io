import * as params from '@params';

const input = document.getElementById('searchInput');
const results = document.getElementById('searchResults');
const status = document.getElementById('searchStatus');
let fuse;
let timer;

function search() {
  const query = input.value.trim();
  results.replaceChildren();
  if (!query) {
    status.textContent = 'Busque nos títulos, textos, categorias e tags.';
    return;
  }
  if (query.length < 2) {
    status.textContent = 'Digite pelo menos duas letras.';
    return;
  }
  const matches = fuse.search(query, { limit: 20 });
  status.textContent = matches.length ? `${matches.length} resultado(s) para “${query}”.` : `Nenhuma publicação encontrada para “${query}”.`;
  for (const { item } of matches) {
    const li = document.createElement('li');
    const a = document.createElement('a');
    a.href = item.permalink;
    a.textContent = item.title;
    li.append(a);
    results.append(li);
  }
}

window.addEventListener('load', async () => {
  try {
    const response = await fetch('../index.json');
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    const data = await response.json();
    const options = params.fuseOpts || {};
    fuse = new Fuse(data, {
      keys: options.keys || ['title', 'summary', 'content', 'categories', 'tags'],
      ignoreLocation: options.ignorelocation ?? true,
      threshold: options.threshold ?? 0.35,
      minMatchCharLength: options.minmatchcharlength ?? 2,
    });
    input.disabled = false;
    status.textContent = data.length ? 'Busque nos títulos, textos, categorias e tags.' : 'As primeiras publicações vêm aí. Por enquanto, explore as categorias e a página Sobre.';
  } catch {
    status.textContent = 'Não foi possível carregar a busca. Recarregue a página ou navegue pelo arquivo.';
  }
});

input.addEventListener('input', () => {
  clearTimeout(timer);
  timer = setTimeout(search, 150);
});
input.addEventListener('search', () => { if (fuse) search(); });
document.getElementById('searchbox').addEventListener('keydown', event => {
  const links = Array.from(results.querySelectorAll('a'));
  const index = links.indexOf(document.activeElement);
  if (event.key === 'ArrowDown' && links.length) {
    event.preventDefault();
    links[Math.min(index + 1, links.length - 1)].focus();
  } else if (event.key === 'ArrowUp') {
    event.preventDefault();
    (index <= 0 ? input : links[index - 1]).focus();
  } else if (event.key === 'Escape' && fuse) {
    input.value = '';
    search();
    input.focus();
  } else if (event.key === 'Enter' && fuse) {
    const query = input.value.trim();
    if (query.length >= 2 && typeof window.__phSearch === 'function') {
      window.__phSearch(query.length);
    }
  }
});

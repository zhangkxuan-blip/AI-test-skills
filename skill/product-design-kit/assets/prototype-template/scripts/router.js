/**
 * 极简哈希路由
 * 用法：在 index.html 引入后，链接写 <a href="#/list">
 */
window.AppRouter = {
  routes: {
    '#/':       'pages/home.html',
    '#/home':   'pages/home.html',
    '#/list':   'pages/list.html',
    '#/detail': 'pages/detail.html',
    '#/form':   'pages/form.html',
    '#/me':     'pages/me.html',
  },

  init(frameId = 'app-frame') {
    const frame = document.getElementById(frameId);
    if (!frame) return console.error('[router] frame not found:', frameId);

    const navigate = () => {
      const path = location.hash || '#/';
      const target = this.routes[path] || this.routes['#/'];
      frame.src = target;
    };

    navigate();
    window.addEventListener('hashchange', navigate);
  }
};

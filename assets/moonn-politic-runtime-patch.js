(function () {
  'use strict';

  var OLD_POLICY_URL = 'https://moonn.ru/politic';
  var NEW_POLICY_URL = 'https://xn--l1acaw.xn--p1ai/politic';
  var TITLE = 'Политика обработки персональных данных | Татьяна Мунн';
  var DESCRIPTION = 'Политика обработки персональных данных сайта Татьяны Мунн: оператор, формы заявок, cookies, Яндекс.Метрика, Webvisor и порядок обращений.';

  function replaceTextNode(node) {
    if (!node || !node.nodeValue || node.nodeValue.indexOf(OLD_POLICY_URL) === -1) return;
    node.nodeValue = node.nodeValue.split(OLD_POLICY_URL).join(NEW_POLICY_URL);
  }

  function walkText(root) {
    var walker = document.createTreeWalker(root || document.body, NodeFilter.SHOW_TEXT);
    var nodes = [];
    while (walker.nextNode()) nodes.push(walker.currentNode);
    nodes.forEach(replaceTextNode);
  }

  function setMeta(selector, attr, value) {
    var node = document.querySelector(selector);
    if (node) node.setAttribute(attr, value);
  }

  function patchLinks() {
    Array.prototype.slice.call(document.querySelectorAll('a[href="' + OLD_POLICY_URL + '"]')).forEach(function (link) {
      link.setAttribute('href', NEW_POLICY_URL);
    });
  }

  function patchHead() {
    document.title = TITLE;
    setMeta('meta[name="description"]', 'content', DESCRIPTION);
    setMeta('meta[property="og:url"]', 'content', NEW_POLICY_URL);
    setMeta('meta[property="og:title"]', 'content', TITLE);
    setMeta('meta[property="og:description"]', 'content', DESCRIPTION);
    setMeta('link[rel="canonical"]', 'href', NEW_POLICY_URL);
  }

  function apply() {
    if (window.location.pathname.replace(/\/+$/, '') !== '/politic') return;
    patchHead();
    patchLinks();
    walkText(document.body);
    document.documentElement.setAttribute('data-moonn-politic-runtime-patch', '2026-06-14');
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', apply);
  } else {
    apply();
  }
})();

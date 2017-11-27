var options = {
  el: '#app',
  delimiters: ['[', ']'],
  data: {
    'drawer': false,
    'usergp': {
      'active': false,
      'list': []
    },
    'routes': [
      {
        'path': '/store',
        'title': 'Store',
        'action': 'store'
      },
      {
        'path': '/cart',
        'title': 'Cart',
        'action': 'shopping_cart'
      }
    ]
  },
  methods: {
  }
};

Vue.filter('moment', (date, format='YYYY/MM/DD hh:mm a') => moment(date).format(format));

Vue.filter('joins', (a, prop='name', sep='; ') => a.map(i => i[prop]).join(sep));

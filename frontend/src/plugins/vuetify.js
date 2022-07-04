import Vue from 'vue';
import Vuetify from 'vuetify/lib/framework';

Vue.use(Vuetify);

export default new Vuetify({
    theme: {
        dark : true,
        themes: {
          dark: {
            primary: '#36DCA4',
            secondary: '#083244',
            accent: '#FFFFFF',
            error: '#b71c1c',
          },
        },
      },

});

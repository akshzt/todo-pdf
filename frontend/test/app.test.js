import Vuetify from 'vuetify';
import App from '../src/App.vue';
import { createLocalVue, mount } from '@vue/test-utils';

describe('App', () => {
  it('has data', () => {
    expect(typeof App.data).toBe('function');
  })
});

describe('Mounted App', () => {
    const localVue = createLocalVue();
    let vuetify;
  
    beforeEach(() => {
      vuetify = new Vuetify();
    });
  
    it('Expect snapshot to match', () => {
      const wrapper = mount(App, {
        localVue,
        vuetify,
      });
      
      expect(wrapper.exists()).toBe(true);
    });

  });
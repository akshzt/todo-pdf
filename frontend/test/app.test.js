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
    let wrapper;

    beforeEach(() => {
      vuetify = new Vuetify();

      wrapper = mount(App, {
        localVue,
        vuetify,
      });
    });
  
    it('Expect snapshot to match', () => {
      expect(wrapper.exists()).toBe(true);
    });

});

import Vuetify from 'vuetify';
import HomeView from '../src/views/HomeView.vue';
import { createLocalVue, mount } from '@vue/test-utils';

describe('App', () => {
  it('has data', () => {
    expect(typeof HomeView.data).toBe('function');
  })
});

describe('Mounted App', () => {
    const localVue = createLocalVue();
    let vuetify;
    let wrapper;

    beforeEach(() => {
      vuetify = new Vuetify();

      wrapper = mount(HomeView, {
        localVue,
        vuetify,
      });
    });
  
    it('Expect snapshot to match', () => {
      expect(wrapper.exists()).toBe(true);
    });

    it('adding task to task list', async() => {
        wrapper.setData({ list: [{ id: 4, task: "JEST TEST TASK 1"}]});
        await wrapper.vm.$nextTick();
        expect(wrapper.text()).toContain('JEST TEST TASK 1');
    });

  });
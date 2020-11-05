import Vue from 'vue';
import { mount } from '@vue/test-utils'
import Button from '@/components/Button.vue'


describe('Button component', () => {
    const wrapper = mount(Button);
    it('clicking .action-button button emits "button-click"', () => {
        wrapper.find('.action-button').childAt(0).simulate('click');
        expect(wrapper.emitted('button-click')).toBeTruthy();
    })
})
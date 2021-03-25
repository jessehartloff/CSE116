document.write(`
<!--<div class="custom-control custom-switch">-->
<!--<input type="checkbox" class="custom-control-input" id="darkSwitch">-->
<!--<label class="custom-control-label" for="darkSwitch">Dark Theme</label>-->
<!--</div>-->

<!-- Rounded switch from https://www.w3schools.com/howto/howto_css_switch.asp -->

<label class="switch">
  <input type="checkbox" id="darkSwitch">
  <span class="slider round"></span>
  <label for="darkSwitch" class="indented-checkbox-text">Dark Theme</label>
</label>

`);

const darkSwitch = document.getElementById('darkSwitch');

darkSwitch.checked = getTheme() === 'dark';
darkSwitch.onchange = () => {
	setTheme(darkSwitch.checked ? 'dark' : 'light');
};

themeChangeHandlers.push(theme => darkSwitch.checked = theme === 'dark');

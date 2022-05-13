var GameJam = document.querySelector('open');
var modal_container = document.querySelector('modal_container')
var close = document.getElementById('close')

GameJam.addEventListener('click', () => {
	modal_container.classList.add('show');

});

close.addEventListener('click', () => {
	modal_container.classList.remove('show');

});
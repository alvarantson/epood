function loader() {
	$(".loader").fadeIn(500);
};
$( document ).ready(function() {
    $(".loader").fadeOut(600);
});


$("#desktop-shopping-cart").on('click', function() {
	$('#desktop-shopping-cart').toggleClass('active');
	$(".desktop-navbar-shopping-cart").toggleClass("hidden");
});
$("#desktop-lang-select").on('click', function() {
	$('#desktop-lang-select').toggleClass('active');
	$(".desktop-navbar-lang-select").toggleClass("hidden");
});
$("#desktop-navbar-categories").on('click', function() {
	$('#desktop-navbar-categories').toggleClass('active');
	$(".desktop-navbar-categories-select").toggleClass("hidden");
});


if( /Android|webOS|iPhone|iPad|iPod|BlackBerry/i.test(navigator.userAgent) ) {
	$(".main").toggleClass("phone-main");
	$(".footer").toggleClass("phone-footer");
	$("nav.shadow").toggleClass("hidden");
	$(".phone-menu-button").toggleClass("hidden");
	$(".phone-cart-button").toggleClass("hidden");
	$(".desktop-navbar-spacer").toggleClass("hidden");
} else {
};

$(".phone-menu-button").on('click', function() {
	$(".phone-menu-button").toggleClass("phone-menu-button-inverted");
	$(".phone-navbar").toggleClass("hidden");
});
$(".phone-cart-button").on('click', function() {
	$(".phone-cart-button").toggleClass("phone-menu-button-inverted");
	$(".phone-cart").toggleClass("hidden");
});
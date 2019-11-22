// Mobile Responsive JS

function showMenu() {
  var x = document.getElementById("menu-icon");
  if (x.className === "icon") {
    x.className += ".responsive";
  } else {
    x.className = "icon";
  }
  var y = document.getElementById("nav-minus-menu");
  if (y.className === "nav-minus-menu"){
  	y.className += ".responsive";
  } else {
  	y.className = "nav-minus-menu"
  }
}
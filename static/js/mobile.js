// Mobile Responsive JS

function showMenu() {
var x = document.getElementById("menu-icon");
  if (x.className === "icon") {
    x.className += "-responsive";
  } else {
    x.className = "icon";
  }
}

function dropMenuItems(){
		var items = [];
		var myPosts = document.getElementById("nav-mobile").getElementsByTagName("a");
		for (var i = 0; i < myPosts.length; i++){
			if(myPosts[i].id.lastIndexOf("listitem", 0) === 0){
				if(myPosts[i].className === "listitem"){
					myPosts[i].className += "-responsive";
				}
				else{
					myPosts[i]. className = "listitem"
				}
				
			}
		}
}


// code taken from https://codepen.io/bbennett/pen/LgLxBx
document.addEventListener("DOMContentLoaded", function() {
  var elems = document.querySelectorAll(".tap-target");
  M.TapTarget.init(elems);
});

function openDiscovery() {
  var inst;
  // Get each of the elements
  var elems = document.querySelectorAll(".tap-target");
  console.log(elems);
  inst = M.TapTarget.getInstance(elems[0]);
  inst.open();
}

// Close any open targets at the end of the process.
function closeAll() {
  $(".tap-target").tapTarget("close");
  $(".tap-target").tapTarget("destroy");
}

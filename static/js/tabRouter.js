routeTabs = destGetParemeter => {
  if (destGetParemeter == "destination_not_set") {
    return;
  }
  $(".tabs").tabs("select", destGetParemeter);
};

updateTabs = () => {
  $(".tabs").tabs("updateTabIndicator");
};

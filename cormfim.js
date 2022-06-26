var realConfirm=window.confirm;
window.confirm=function(){
  window.confirm=realConfirm;
  return true;
};

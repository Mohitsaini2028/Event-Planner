function borderHeart(x){
  var id = x.id;
  id = id.match(/(\d+)/);
  id = id[0];

  const form = document.getElementById('likeForm');
  form.action="like/";

  document.getElementById('eventId').value=id;
  console.log(id)
  form.submit();
}

function fillHeart(x){

  var id=x.id;
  id = id.match(/(\d+)/);
  id = id[0];

  const form = document.getElementById('likeForm');
  form.action="unlike/";
  document.getElementById('eventId').value=id;
  form.submit();

}

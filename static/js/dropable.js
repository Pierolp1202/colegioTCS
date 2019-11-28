function allowDrop(ev) {
  ev.preventDefault();
}

function drag(ev) {
  ev.dataTransfer.setData("text", ev.target.id);
}

function drop(ev) {
  ev.preventDefault();
  var data = ev.dataTransfer.getData("text");
  var node = setHours(document.getElementById(data).cloneNode(true));
  ev.target.appendChild(node);
}

function setHours(node) {
  let inicio = prompt("Hora de inicio:");
  let fin = prompt("Hora de fin:");
  let patron = new RegExp(/\d?\d?:\d?\d?/);
  let para = document.createElement("p");
  if(!patron.test(inicio)){
      inicio="__:__";
  }
  if(!patron.test(fin)){
    fin="__:__";
}
  para.appendChild(document.createTextNode(`${inicio} - ${fin}`));
  node.replaceChild(para, node.children[2]);
  return node;
}

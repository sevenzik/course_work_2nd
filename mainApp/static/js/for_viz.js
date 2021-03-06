$(document).ready(function () {
    var count =  $('#count').val();

    for (var i = 1; i <= count; i++)
    {
        let svg_div = $('#graphviz_svg'+i.toString());//вообще нужен массив id
        let data = $('#data'+i.toString()).val();//вообще нужен массив графов

        let task_source =  $('#task_source'+i.toString()).val();

        $('#exactly_task'+i.toString()).html(task_source)

        // Generate the Visualization of the Graph into "svg".
        let viz = new Viz();
        viz.renderSVGElement(data)
          .then(function(element) {
            svg_div.html(element);
          })
          .catch(error => {
            viz = new Viz();
            console.error(error);
          });
    }

    document.getElementById('cbp-fwslider').style.display = "block";
    document.getElementById('loading').style.display = "none";
})
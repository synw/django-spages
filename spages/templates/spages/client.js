{% include "spages/spagelib/page.js" %}
{% include "spages/spagelib/promise.min.js" %}
function loadPage(resturl){
	var container = 'content';
	{% include "spages/extra_handlers.js" %}
	promise.get(resturl,{},{"Accept":"application/json"}).then(function(error, data, xhr) {
	    if (error) {console.log('Error ' + xhr.status);return;}    
	    var parsed_data = JSON.parse(data);
	    var content = parsed_data.content;
	    var title = parsed_data.title;
	    top.document.title = title;
	    top.document.getElementById(container).innerHTML = content;
	    {% include "spages/extra_async_handlers.js" %}
	});
	return
}
{% include "spages/auto/routes.js" %}
page();
</script>
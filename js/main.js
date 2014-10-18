var xhr;
status();
function ajaxcall(url)
{
	xhr= new XMLHttpRequest();
	xhr.open('GET', url, true);
	xhr.onreadystatechange = function () {
		if(xhr.readyState == 4)
		{	
			var resp = JSON.parse(xhr.responseText);
			present(resp);
		}
	}
	xhr.send();
}

function present(response)
{
	if(response.status)
	{
		document.getElementById('imageholder').innerHTML='<img id="on" src="images/img_trans.gif">';
	}
	else
	{
		document.getElementById('imageholder').innerHTML=' <img id="off" src="images/img_trans.gif">';
	}
}

function status()
{
	ajaxcall('/status');
}

function toggle()
{
	ajaxcall('/do');
}
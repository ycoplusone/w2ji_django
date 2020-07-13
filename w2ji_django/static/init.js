/* 
 * title   		: js global function
 * content 		: 공통 js function을 등록한다. 
 * name    		: 송원일(ycoplusone@gmail.com)
 * create date	: 2018.02.01
 */
var _global;

function getSearch(){	//조회 조건 검색하기
	var contents = $('#search_item').children();
	var contents_size = contents.length;
	var param = new Object();
	//console.log('param',param);
	for(var i=0; i<contents_size; i++){
		if( contents.eq(i)[0].id != '' ){
			var param_id =contents.eq(i)[0].id;
			var	param_value = contents.eq(i).val();
			if( param_id.indexOf('d2d') >= 0 ){	//일자의 경우 하이픈을 제거한다.				
				param[ param_id ] = param_value.replace(/-/g,"");	//전체 하이픈을 저거한다.
			}else if( param_id.indexOf('day') >= 0 ){	// 월의 경우 하이픈을 제거한다		
				param[ param_id ] = param_value.replace(/-/g,"");	//전체 하이픈을 저거한다.
			}else if( param_id.indexOf('month') >= 0 ){	// 월의 경우 하이픈을 제거한다				
				param[ param_id ] = param_value.replace(/-/g,"");	//				
			}else{				
				param[ param_id ] = param_value;				
			}			
			//console.log(contents.eq(i)[0].id ,  );
		}	 
	}
	//console.log('_global : ',param);
	return param;
}

function filedownload(url, parm){	//파일 다운로드 action
	  var agent = navigator.userAgent.toLowerCase();
	
	  var f = document.createElement('form');
	  var objs, value;
	  for (var key in parm) {		
	    value = parm[key];
	    objs = document.createElement('input');
	    objs.setAttribute('type', 'hidden');
	    objs.setAttribute('name', key);
	    objs.setAttribute('value', value);
	    f.appendChild(objs);
	  }
	  if(agent.indexOf("msie") != -1){
		  window.open('', "popupview", "width=0, height=0, top=0, statusbar=no, scrollbars=no, toolbar=no").close(); 
		  f.setAttribute('target', 'popupview');
	  }else{
		  f.setAttribute('target', '_blank');
	  }
	  
	  f.setAttribute('method', 'post');
	  f.setAttribute('action', url);
	  document.body.appendChild(f);
	  f.submit();
}

function pdfdownload( url, parm ){	//PDF 다운로드
	/*var popup = window.open(url, "popupview", "width=0, height=0, top=0, statusbar=no, scrollbars=no, toolbar=no");
	  popup.focus(); */
	var agent = navigator.userAgent.toLowerCase();

	alert( "크롬 브라우저입니다." );
	/*if (agent.indexOf("chrome") != -1) {
		alert("크롬 브라우저입니다.");
	}*/
}


//숫자 색 넣기
function num_color(num ){
    if (val > 105427024){
        return '<span style="color:red;">('+val+')</span>';
    } else {
        return '<span style="color:blue;">('+val+')</span>';
    }
}

//숫자 콤마 넣기
function num_comma( num ){	
	if(typeof  num === 'undefined'){
		return '';
	}	
	var parts = (num+'').split(".");	
	parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
	return parts.join(".");	
}

//start of getChartData
function getChartData(url , param){
	var temp = "";
    $.ajax({
        type 		: 'POST',
        dataType 	: 'json',
        url 		: url 	,
       	data 		: param ,
       	async		: false	,  
       	success 	: function(json){
       			temp = json;
       	} ,	error : function( err ){}
    });	
    return temp;
}
//end of getChartData


//start of c3Chart
function c3Chart( data , json ){ //     							
	var bindto 		= data[0];	//바인드 ID
	var label 		= data[1];	//레이블	
	var dataset 	= data[2];	//데이터 셋
	var groups 		= data[3];	//그룹

	var category 	= [];//['cat1', 'cat2', 'cat3', 'cat4', 'cat5', 'cat6','aaa'];
	var types 		= {};//{ data3: 'spline', 오잉: 'line', 비율 : 'area'  };
	var data 		= [];
	var axes 		= {};
	
	for(var i in dataset){
		var row = dataset[i];
		data[i] = new Array();
		if(row[3]!= 'bar'){
			types[row[1]] = row[3];	//차트종류 결정
		}
		if( row[2] == 'y2' ){
			axes[row[1]] = 'y2';
		}
		data[i][0] = row[1];	//범례 추가    						       			
	}
	
	for(var i in json.rows ){	//데이터 바이딩               			
		category[i] = (json.rows[i][label[0]] );	//label 추가
		for(var j in dataset){    						       				
			data[j][ (Number(i) + 1) ] = (json.rows[i][dataset[j][0]] );	//데이터
		}    						       			
	}
	
	//console.log('data', data);
	//console.log('groups', groups);
	
	c3.generate({
		bindto		: '#'+bindto,
	    grid		: { x: { show: label[2].grid }, y: { show : label[2].grid }  },
	    padding		: label[3] , //{	top : label[3].top , left : label[3].left , right : label[3].right , bottom : label[3].bottom   },
	    data: {
	        columns : data ,
	        type 	: 'bar',
	        types 	: types ,
	        groups	: [ groups ] ,
	        axes 	: axes
	    } ,
	    
	    legend: { show : label[2].legend , position : 'right' } ,
	    
	    axis : {
	    	x : {
	    		show 		: label[2].xaxis , 
	            type		: 'category' ,
	            categories	: category
	        } ,
	        y : {
	        	show		: label[2].yaxis ,
	            tick		: { format	: d3.format(",") }
	        } ,
	        y2 : {
	        	show		: false ,
	        	tick		: { format: d3.format(",.1r") }
	        }
	    } ,
	    color: {
	        pattern: ['#1f77b4', '#aec7e8', '#ff7f0e', '#ffbb78', '#2ca02c', '#98df8a', '#d62728', '#ff9896', '#9467bd', '#c5b0d5', '#8c564b', '#c49c94', '#e377c2', '#f7b6d2', '#7f7f7f', '#c7c7c7', '#bcbd22', '#dbdb8d', '#17becf', '#9edae5']
	    } ,
	    tooltip: {
	        format: {
	            value: function (value, ratio, id) {
	                var format = d3.format(',');
	                return format(value);
	            }
	        }
	    }    		    						    
	});      						       		


}// end of c3Chart

// start of c3Donut
function c3Donut( data , json ){
	var bindto 		= data[0];	//바인드 ID
	var setup 		= data[1];	//설정
	var dataset 	= data[2];	//데이터 셋
	var data 		= [];
	for(var i in dataset){
		var row = dataset[i];
		data[i] = new Array();
		data[i][0] = row[1];	//범례 추가    						       			
	}
	
	for(var i in json.rows ){	//데이터 바이딩               			
		for(var j in dataset){    						       				
			data[j][ (Number(i) + 1) ] = (json.rows[i][dataset[j][0]] );	//데이터
		}    						       			
	}
	
	c3.generate({
		bindto 	: '#'+bindto ,
		padding	: setup[1] , //{	top : 20 , left : 20 , right : 20 , bottom : 20   } ,
	    data	: {
	    	type 	: 'donut' ,
	        columns	: data     						        
	    },
	    legend	: setup[0].legend , //{ show : false , position : 'right' } ,
	    donut	: setup[0].donut 	//{ title	: "도넛차트" }
	});
}//end of c3Donut

//start of c3Pie
function c3Pie( data , json ){
	var bindto 		= data[0];	//바인드 ID
	var setup 		= data[1];	//설정
	var dataset 	= data[2];	//데이터 셋
	var data 		= [];
	
	for(var i in dataset){
		var row = dataset[i];
		data[i] = new Array();
		data[i][0] = row[1];	//범례 추가    						       			
	}
	
	for(var i in json.rows ){	//데이터 바이딩               			
		for(var j in dataset){    						       				
			data[j][ (Number(i) + 1) ] = (json.rows[i][dataset[j][0]] );	//데이터
		}    						       			
	}
	
	c3.generate({
		bindto 	: '#'+bindto ,
		legend	: setup[0].legend , //{ show : false , position : 'right' } ,
		padding	: setup[1] ,	//{	top : 20 , left : 20 , right : 20 , bottom : 20   },
	    data	: {
	    	type 	: 'pie' ,
	        columns	: data  						        
	    }
	});
	
}
//end of c3Pie

//start of c3Gauge
function c3Gauge( data , json ){
	var bindto 		= data[0];	//바인드 ID
	var setup 		= data[1];	//설정
	var dataset 	= data[2];	//데이터 셋
	var data 		= [];
	
	for(var i in dataset){
		var row = dataset[i];
		data[i] = new Array();
		data[i][0] = row[1];	//범례 추가    						       			
	}
	
	for(var i in json.rows ){	//데이터 바이딩               			
		for(var j in dataset){    						       				
			data[j][ (Number(i) + 1) ] = (json.rows[i][dataset[j][0]] );	//데이터
		}    						       			
	}
	
	c3.generate({
		bindto 	: '#'+bindto ,
		legend	: setup[0].legend , //{ show : false , position : 'right' } ,
	    data	: {
	    	type	: 'gauge' ,
	        columns	: data				        
	    },
	    gauge : {
	    	max 	: setup[0].max ,	    	 
	    	label	: {
	    		show: true
			}
	    },
	    color	: {
	        pattern		: setup[0].pattern , //['#FF0000', '#F97600', '#F6C600', '#60B044'] , // the three color levels for the percentage values.
	        threshold	: {    						        	
	        	values	: setup[0].values 	//[30, 60, 90, 120] 
	    	}
	    } ,
	    tooltip: {
	    	show : false
	    }
	    //, size : { height: 250 }
	});	
}
//end of c3Gauge

// start of html2canver
function  html2png(){
	html2canvas(document.body).then(function(canvas) {
		var imgObj = new Image();
	    	var base64image = canvas.toDataURL("image/png");
			imgObj.src = base64image;
			
			var d = new Date();
			var date_str = d.getFullYear(); 
				date_str = date_str+'.'+(d.getMonth() + 1);
				date_str = date_str+'.'+d.getDate();
				date_str = date_str+'-'+d.getHours();
				date_str = date_str+d.getMinutes();
				date_str = date_str+d.getSeconds();

			imageWin = window.open("", "imageWin" , "width=1024 , height= 630");
			imageWin.document.write("<html><body style='margin:0'>") ;
			imageWin.document.write("<img src = '" + imgObj.src + "' style='max-width : 1000px ; max-height : 540px ' >") ;
			imageWin.document.write("<br/><center> <button><a href='"+imgObj.src+"' download='캡쳐_"+date_str+".png' style='color: black ; text-decoration:none' >다운로드</a></button>") ;
			imageWin.document.write("　<button><a class='btn' onclick='self.close();' >닫기</a></button>") ;
			imageWin.document.write("</center>") ;		
			imageWin.document.write("</body><html>") ;
	});  		
}
// end of html2canver


function getParameter(param) {	// request 파라미터 값 가져오기.
    var returnValue;
    var url = location.href;
    var parameters = (url.slice(url.indexOf('?') + 1, url.length)).split('&');
    for (var i = 0; i < parameters.length; i++) {
        var varName = parameters[i].split('=')[0];
        if (varName.toUpperCase() == param.toUpperCase()) {
            returnValue = parameters[i].split('=')[1];
            return decodeURIComponent(returnValue);
        }
    }
};


(function () {
	_global ={ 
			root : window.location.pathname.substring(0, window.location.pathname.indexOf('/',2))
			, company_id : sessionStorage.getItem('company_id')
    	 	, group_id : sessionStorage.getItem('group_id')
    		, user_id : sessionStorage.getItem('user_id')
    		, user_nm : sessionStorage.getItem('user_nm')
    		, max_file_size : 10240000
    		, max_file_nm : '10MB이상은 업로드 할수 없습니다.'
	}
	
}());
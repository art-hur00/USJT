function lerXML(){
   var req = new XMLHttpRequest();
 
   req.onreadystatechange = function(){
       if( this.readyState == 4 && this.status == 200){       
           txt = this.responsetxt + "<hr>";   

           var dadosXML = this.responseXML; 

           txt += dadosXML.getElementsByTagName("marca");
           txt += marcas[0].childNodes[0].nodeValue + "<br>";
           txt += "<br>Modelo:" + dadosXML.getElementsByTagName("modelo");

           var tagCores = dadosXML.getElementsByTagName("cores");
           var cores = tagCores[0].getElementsByTagName("cor");
           for( var i = 0; i < cores.length; i++){
               txt +=  cores[i].childNodes[0].nodeValue + " - ";
           }   


           document.getElementById("divXML").innerHTML = txt;
          
           }   
       }

       req.open( "GET" , "dados.xml" , true );
       req.send();
}
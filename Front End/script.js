
function Predict () {
 

  var data=0;
  var city1 =
   document.getElementById("city").value;

  var date1 =
   document.getElementById("date1").value;

  var time1 =
   document.getElementById("time1").value;
   
   if(city1=== "naha"){

      if(date1==="2020-11-19" & time1==="060000"){
        data=0.22822961314619558;
      }
      if(date1==="2020-11-20" & time1==="170000")
      {
        data=0.13906219945823953;
      }
      if(date1==="2020-11-20" & time1==="200000")
      {
        data=0.1336191478211305;
      }
    
   }
   if(city1=="sendai")
   {
      if(date1==="2020-11-19" & time1==="183000")
      {
        data=0.021350371578241763;
      }
   }
   if(city1=="nigata")
   {
    if(date1==="2020-11-19" & time1==="230000")
    {
      data=0.10497764087733627;
    }
   }

   
   if(data!==0)
   {
   var message = "<h2>The Predicted Rainfall is " + data + " mm/hr</h2>";
  }
    else
    {
      var message="<h2>Hurrah!!! NO Rain :)</h2>"
    }

  // document
  //   .getElementById("content")
  //   .textContent = message;

  document
    .getElementById("content")
.innerHTML = message;


}
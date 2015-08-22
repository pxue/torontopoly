
var moneyCard = '<div class="card" style="display: inline-block; vertical-align: top">\
 <div class="card-inner">\
  <div class="bank-value rotate-90">\
   <div class="bank-value-inner">\
    <span class="currency"></span><span class="amount"></span>\
   </div>\
  </div>\
  <div class="" style="margin: 2%; border: 4px double #ccc; height: 94%;">\
   <table style="height: 100%; width: 100%; text-align: center">\
    <tbody><tr>\
     <td class="">\
       <div class="money rotate-90">\
        <span class="currency"></span><span class="amount"></span>\
      </div>\
     </td>\
    </tr>\
   </tbody></table>\
  </div>\
  <div class="bank-value bottom rotate-90">\
   <div class="bank-value-inner">\
    <span class="currency"></span><span class="amount"></span>\
   </div>\
  </div>\
 </div>\
</div>';

var rentCard = '<div class="card" style="display: inline-block; vertical-align: top">\
 <div class="card-inner">\
  <div class="bank-value rotate-90">\
   <div class="bank-value-inner">\
    <span class="currency"></span><span class="amount"></span>\
   </div>\
  </div>\
  <div class="" style="margin: 2%; border: 4px double #ccc; height: 94%;">\
   <table style="height: 100%; width: 100%; text-align: center">\
    <tbody><tr>\
     <td class="">\
      <div class="" style="margin: 0 auto; border-radius: 50%; border: 4px solid #111;">\
       <div style="height: 4em; margin: 3.5em auto;"><span id="title" style="text-transform: uppercase; font-weight: bold; font-size: 2.25em; line-height: 0.9em; margin: 0 auto; display: block; max-width: 3em">RENT</span></div>\
      </div>\
     </td>\
    </tr>\
   </tbody></table>\
  </div>\
  <div class="bank-value bottom rotate-90">\
   <div class="bank-value-inner">\
    <span class="currency"></span><span class="amount"></span>\
   </div>\
  </div>\
 </div>\
</div>';


var actionCard = '<div class="card" style="display: inline-block; vertical-align: top">\
 <div class="card-inner">\
  <div class="bank-value rotate-90">\
   <div class="bank-value-inner">\
    <span class="currency"></span><span class="amount"></span>\
   </div>\
  </div>\
  <div class="" style="margin: 2%; border: 4px double #ccc; height: 94%;">\
   <table style="height: 100%; width: 100%; text-align: center">\
    <tbody><tr>\
     <td class="">\
      <div class="" style="position: absolute; top: 15%; left: 0; right: 0; text-transform: uppercase; font-weight: bold; font-size: 1.25em">ACTION CARD</div>\
      <div class="" style="margin: 0 auto; border-radius: 50%; border: 4px solid #111;">\
       <div style="height: 4em; margin: 3.5em auto;"><span id="title" style="text-transform: uppercase; font-weight: bold; font-size: 2.25em; line-height: 0.9em; margin: 0 auto; display: block; max-width: 3em"></span></div>\
      </div>\
      <div id="desc" style="position: absolute; bottom: 8%; left: 0; right: 0; margin: 0 auto; line-height: 1.25em; color: #555; font-size: 75%">\
       <div>Play into center to use.</div>\
      </div>\
     </td>\
    </tr>\
   </tbody></table>\
  </div>\
  <div class="bank-value bottom rotate-90">\
   <div class="bank-value-inner">\
    <span class="currency"></span><span class="amount"></span>\
   </div>\
  </div>\
 </div>\
</div>';

var twoRentProperty = '<div class="card" style="display: inline-block; vertical-align: top">\
 <div class="card-inner">\
  <div class="title">\
   <div>\
    <div>\
     <div id="title-div"></div>\
    </div>\
   </div>\
  </div>\
  <div class="bank-value">\
   <div class="bank-value-inner">\
    <span class="currency"></span><span class="amount"></span>\
   </div>\
  </div>\
  <table class="rent-rate">\
   <tbody><tr class="header-row">\
    <td colspan="2" class="help-heading">(No. of properties owned in set)</td>\
    <td></td>\
    <td colspan="2" class="rent-heading">RENT</td>\
   </tr>\
   <tr>\
    <td class="set-count">\
     <div class="set-count-inner">\
      <div class="set-count-card set-count-card-4">\
       <div class="set-count-card-top"></div>\
       <div class="set-count-card-content">1</div>\
      </div>\
     </div>\
    </td>\
    <td class="filler" colspan="3">\
     <div><div><div></div></div></div>\
    </td>\
    <td class="rent-rate">\
     <div class="rent-rate">\
      <span class="currency"></span><span class="amount"></span>\
     </div>\
    </td>\
   </tr>\
   <tr>\
    <td class="set-count">\
     <div class="set-count-inner">\
      <div class="set-count-card set-count-card-3">\
       <div class="set-count-card-top"></div>\
       <div class="set-count-card-content">1</div>\
      </div>\
      <div class="set-count-card set-count-card-4">\
       <div class="set-count-card-top"></div>\
       <div class="set-count-card-content">2</div>\
      </div>\
     </div>\
    </td>\
    <td class="filler" colspan="3">\
     <div><div><div></div></div></div>\
    </td>\
    <td class="rent-rate">\
     <div class="rent-rate">\
      <span class="currency"></span><span class="amount"></span>\
     </div>\
    </td>\
   </tr>\
   <tr>\
    <td class="full-set"><div><span>FULL SET</span></div></td>\
   </tr>\
  </tbody></table>\
 </div>\
</div>';

var threeRentProperty = '<div class="card" style="display: inline-block; vertical-align: top">\
 <div class="card-inner">\
  <div class="front">\
  <div class="title" style="background-color: #">\
   <div>\
    <div>\
     <div id="title-div"></div>\
    </div>\
   </div>\
  </div>\
  <div class="bank-value">\
   <div class="bank-value-inner">\
    <span class="currency"></span><span class="amount"></span>\
   </div>\
  </div>\
  <table class="rent-rate">\
   <tbody><tr class="header-row">\
    <td colspan="2" class="help-heading">(No. of properties owned in set)</td>\
    <td></td>\
    <td colspan="2" class="rent-heading">RENT</td>\
   </tr>\
   <tr>\
    <td class="set-count">\
     <div class="set-count-inner">\
      <div class="set-count-card set-count-card-4">\
       <div class="set-count-card-top" style="background-color: #"></div>\
       <div class="set-count-card-content">1</div>\
      </div>\
     </div>\
    </td>\
    <td class="filler" colspan="3">\
     <div><div><div></div></div></div>\
    </td>\
    <td class="rent-rate">\
     <div class="rent-rate">\
      <span class="currency"></span><span class="amount"></span>\
     </div>\
    </td>\
   </tr>\
   <tr>\
    <td class="set-count">\
     <div class="set-count-inner">\
      <div class="set-count-card set-count-card-3">\
       <div class="set-count-card-top" style="background-color: #"></div>\
       <div class="set-count-card-content">1</div>\
      </div>\
      <div class="set-count-card set-count-card-4">\
       <div class="set-count-card-top" style="background-color: #"></div>\
       <div class="set-count-card-content">2</div>\
      </div>\
     </div>\
    </td>\
    <td class="filler" colspan="3">\
     <div><div><div></div></div></div>\
    </td>\
    <td class="rent-rate">\
     <div class="rent-rate">\
      <span class="currency"></span><span class="amount"></span>\
     </div>\
    </td>\
   </tr>\
   <tr>\
    <td class="set-count">\
     <div class="set-count-inner">\
      <div class="set-count-card set-count-card-2">\
       <div class="set-count-card-top" style="background-color: #"></div>\
       <div class="set-count-card-content">1</div>\
      </div>\
      <div class="set-count-card set-count-card-3">\
       <div class="set-count-card-top" style="background-color: #"></div>\
       <div class="set-count-card-content">2</div>\
      </div>\
      <div class="set-count-card set-count-card-4">\
       <div class="set-count-card-top" style="background-color: #"></div>\
       <div class="set-count-card-content">3</div>\
      </div>\
     </div>\
    </td>\
    <td class="filler" colspan="3">\
     <div><div><div></div></div></div>\
    </td>\
    <td class="rent-rate">\
     <div class="rent-rate">\
      <span class="currency"></span><span class="amount"></span>\
     </div>\
    </td>\
   </tr>\
   <tr>\
    <td class="full-set"><div><span>FULL SET</span></div></td>\
   </tr>\
  </tbody></table>\
  </div>\
  <div class="back">\
  </div>\
 </div>\
</div>';


var railsProperty = '<div class="card" style="display: inline-block; vertical-align: top">\
 <div class="card-inner">\
  <div class="front">\
  <div class="title" style="background-color: #">\
   <div>\
    <div>\
     <div id="title-div" style="color: white"></div>\
    </div>\
   </div>\
  </div>\
  <div class="bank-value">\
   <div class="bank-value-inner">\
    <span class="currency"></span><span class="amount"></span>\
   </div>\
  </div>\
  <table class="rent-rate">\
   <tbody><tr class="header-row">\
    <td colspan="2" class="help-heading">(No. of properties owned in set)</td>\
    <td></td>\
    <td colspan="2" class="rent-heading">RENT</td>\
   </tr>\
   <tr>\
    <td class="set-count">\
     <div class="set-count-inner">\
      <div class="set-count-card set-count-card-4">\
       <div class="set-count-card-top" style="background-color: #"></div>\
       <div class="set-count-card-content">1</div>\
      </div>\
     </div>\
    </td>\
    <td class="filler" colspan="3">\
     <div><div><div></div></div></div>\
    </td>\
    <td class="rent-rate">\
     <div class="rent-rate">\
      <span class="currency"></span><span class="amount"></span>\
     </div>\
    </td>\
   </tr>\
   <tr>\
    <td class="set-count">\
     <div class="set-count-inner">\
      <div class="set-count-card set-count-card-3">\
       <div class="set-count-card-top" style="background-color: #"></div>\
       <div class="set-count-card-content">1</div>\
      </div>\
      <div class="set-count-card set-count-card-4">\
       <div class="set-count-card-top" style="background-color: #"></div>\
       <div class="set-count-card-content">2</div>\
      </div>\
     </div>\
    </td>\
    <td class="filler" colspan="3">\
     <div><div><div></div></div></div>\
    </td>\
    <td class="rent-rate">\
     <div class="rent-rate">\
      <span class="currency"></span><span class="amount"></span>\
     </div>\
    </td>\
   </tr>\
   <tr>\
    <td class="set-count">\
     <div class="set-count-inner">\
      <div class="set-count-card set-count-card-2">\
       <div class="set-count-card-top" style="background-color: #"></div>\
       <div class="set-count-card-content">1</div>\
      </div>\
      <div class="set-count-card set-count-card-3">\
       <div class="set-count-card-top" style="background-color: #"></div>\
       <div class="set-count-card-content">2</div>\
      </div>\
      <div class="set-count-card set-count-card-4">\
       <div class="set-count-card-top" style="background-color: #"></div>\
       <div class="set-count-card-content">3</div>\
      </div>\
     </div>\
    </td>\
    <td class="filler" colspan="3">\
     <div><div><div></div></div></div>\
    </td>\
    <td class="rent-rate">\
     <div class="rent-rate">\
      <span class="currency"></span><span class="amount"></span>\
     </div>\
    </td>\
   </tr>\
   <tr>\
    <td class="set-count">\
     <div class="set-count-inner">\
      <div class="set-count-card set-count-card-1">\
       <div class="set-count-card-top" style="background-color: #"></div>\
       <div class="set-count-card-content">1</div>\
      </div>\
      <div class="set-count-card set-count-card-2">\
       <div class="set-count-card-top" style="background-color: #"></div>\
       <div class="set-count-card-content">2</div>\
      </div>\
      <div class="set-count-card set-count-card-3">\
       <div class="set-count-card-top" style="background-color: #"></div>\
       <div class="set-count-card-content">3</div>\
      </div>\
      <div class="set-count-card set-count-card-4">\
       <div class="set-count-card-top" style="background-color: #"></div>\
       <div class="set-count-card-content">4</div>\
      </div>\
     </div>\
    </td>\
    <td class="filler" colspan="3">\
     <div><div><div></div></div></div>\
    </td>\
    <td class="rent-rate">\
     <div class="rent-rate">\
      <span class="currency"></span><span class="amount"></span>\
     </div>\
    </td>\
   </tr>\
   <tr>\
    <td class="full-set"><div><span>FULL SET</span></div></td>\
   </tr>\
  </tbody></table>\
  </div>\
  <div class="back">\
  </div>\
 </div>\
</div>';

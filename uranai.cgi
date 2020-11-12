#!/usr/bin/perl
 
use CGI;
$uranai = new CGI;
 
$n = int(rand()*4);
 
@otsuge = (
         "か、良い名前じゃ",
         "か、不吉な名前じゃ",
         "か、平凡な名前じゃ",
         "か、画数が良くないな"
         );
 
print $uranai->header(-charset=>'UTF-8'),
  $uranai->start_html(-title=>"占い");
print "<h2>お告げ</h2>\n";
print "<p>", $uranai->param('name'), @otsuge[$n], "</p>\n";
print $uranai->end_html();

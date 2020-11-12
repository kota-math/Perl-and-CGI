#!/usr/bin/perl
 
use CGI;
$uranai = new CGI;
 
$n = int(rand()*8);
 
@otsuge = (
    "今日は最高の一日になりそうじゃ",
    "今日はいいことありそうじゃ",
    "今日はお米を食べるとよさそうじゃ",
    "今日は外に出かけるのじゃ",
    "今日はまずまずの一日じゃ",
    "今日は忘れ物に注意じゃ",
    "今日は慎重に生活するのがよさそうじゃ",
    "今日は早く寝るのじゃ"
    );
$m = $uranai->param('month');
$d = $uranai->param('date');
$b = $uranai->param('bt');
$name = $uranai->param('name');

if(($m==1 && ($d>=20 && $d<=31)) || ($m==2 && ($d>=1 && $d<=18))){
    $seiza="みずがめ座";
}
elsif(($m==2 && ($d>=19 && $d<=29)) || ($m==3 && ($d>=1 && $d<=20))){
    $seiza="うお座";
}
elsif(($m==3 && ($d>=21 && $d<=31)) || ($m==4 && ($d>=1 && $d<=19))){
    $seiza="おひつじ座";
}
elsif(($m==4 && ($d>=20 && $d<=30)) || ($m==5 && ($d>=1 && $d<=20))){
    $seiza="おうし座";
}
elsif(($m==5 && ($d>=21 && $d<=31)) || ($m==6 && ($d>=1 && $d<=21))){
    $seiza="ふたご座";
}
elsif(($m==6 && ($d>=22 && $d<=30)) || ($m==7 && ($d>=1 && $d<=22))){
    $seiza="かに座";
}
elsif(($m==7 && ($d>=23 && $d<=31)) || ($m==8 && ($d>=1 && $d<=22))){
    $seiza="しし座";
}
elsif(($m==8 && ($d>=23 && $d<=31)) || ($m==9 && ($d>=1 && $d<=23))){
    $seiza="おとめ座";
}
elsif(($m==9 && ($d>=24 && $d<=30)) || ($m==10 && ($d>=1 && $d<=23))){
    $seiza="てんびん座";
}
elsif(($m==10 && ($d>=24 && $d<=31)) || ($m==11 && ($d>=1 && $d<=22))){
    $seiza="さそり座";
}
elsif(($m==11 && ($d>=23 && $d<=30)) || ($m==12 && ($d>=1 && $d<=21))){
    $seiza="いて座";
}
elsif(($m==12 && ($d>=22 && $d<=31)) || ($m==1 && ($d>=1 && $d<=19))){
    $seiza="やぎ座";
}
else{
    $seiza="不明";
}

if ($b eq 'A') {
    $bt = "A型";
}
elsif ($b eq 'B') {
    $bt = "B型";
}
elsif ($b eq 'O') {
    $bt = "O型";
}
elsif ($b eq "AB") {
    $bt = "AB型";
}
else {
    $bt = "不明";
}

print $uranai->header(-charset=>'UTF-8'),
  $uranai->start_html(-title=>"占い");
print "<h2>お告げ</h2>\n";
if ($name eq "") {
    print "<p>お主は誰じゃ...??</p>\n";
}
else {
    print "<p>お主は ", $uranai->param('name'),", 血液型は $bt で, 星座は $seiza か,<br> ", @otsuge[$n], "</p>\n";
}
print $uranai->end_html();

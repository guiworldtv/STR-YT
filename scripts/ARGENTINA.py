#! /usr/bin/python3

banner = r'''
###########################################################################
#                                                                         #

#                                  >> https://github.com/guiworldtv       #
###########################################################################

#EXTINF:-1 tvg-id="" tvg-name="SPORTS: TNT SPORTS HD Op1 " tvg-logo="https://w7.pngwing.com/pngs/621/229/png-transparent-superliga-argentina-de-futbol-logo-tnt-sports-logo-sport-text-trademark-logo.png" group-title="DEPORTES",SPORTS: TNT SPORTS HD Op1 
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/94714
#EXTINF:-1 tvg-id="" tvg-name="SPORTS:ESPN 1 DIRECTO ARG" tvg-logo="https://www.futbolenvivo.com.co/wp-content/uploads/2020/01/ESPN-2-en-vivo-online.jpg" group-title="DEPORTES",SPORTS:ESPN 1 DIRECTO ARG
https://delivery.cdn.rcs.net.ar/mnp/espn_hls/playlist.m3u8
#EXTINF:-1 tvg-id="" tvg-name="SPORTS:ESPN 2 DIRECTO ARG" tvg-logo="https://www.futbolenvivo.com.co/wp-content/uploads/2020/01/ESPN-2-en-vivo-online.jpg" group-title="DEPORTES",SPORTS:ESPN 2 DIRECTO ARG
https://delivery.cdn.rcs.net.ar/mnp/espn2_hls/playlist.m3u8
#EXTINF:-1 tvg-id="" tvg-name="SPORTS: :Directv Sports 1 SD" tvg-logo="https://seeklogo.com/images/D/directv-sports-logo-6F86DBD521-seeklogo.com.png" group-title="DEPORTES",SPORTS: :Directv Sports 1 SD
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/53958
#EXTINF:-1 tvg-id="" tvg-name="SPORTS: Directv Sports 1 ARG FHD" tvg-logo="https://seeklogo.com/images/D/directv-sports-logo-6F86DBD521-seeklogo.com.png" group-title="DEPORTES",SPORTS: Directv Sports 1 ARG FHD
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/53959
#EXTINF:-1 tvg-id="" tvg-name="SPORTS: :Directv Sports 1" tvg-logo="https://seeklogo.com/images/D/directv-sports-logo-6F86DBD521-seeklogo.com.png" group-title="DEPORTES",SPORTS: :Directv Sports 1
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/679
#EXTINF:-1 tvg-id="" tvg-name="SPORTS: :DirectvSP 2" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/DirecTV_Sports_2_Latin_America_%282018%29.png/1200px-DirecTV_Sports_2_Latin_America_%282018%29.png" group-title="DEPORTES",SPORTS: :DirectvSP 2
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/680
#EXTINF:-1 tvg-id="" tvg-name="SPORTS: :DirectvSP+ Plus" tvg-logo="https://www.pngfind.com/pngs/m/297-2974594_directv-sports-plus-logo-hd-png-download.png" group-title="DEPORTES",SPORTS: :DirectvSP+ Plus
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/678
#EXTINF:-1 tvg-id="" tvg-name="SPORTS: TYC SPORTS BUENOS AIRES" tvg-logo="https://vignette.wikia.nocookie.net/logopedia/images/d/dc/TYC94.png" group-title="DEPORTES",SPORTS: TYC SPORTS BUENOS AIRES
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/66700
#EXTINF:-1 tvg-id="" tvg-name="SPORTS-ARG: TyC Sports HD" tvg-logo="" group-title="DEPORTES 2",SPORTS-ARG: TyC Sports HD
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/58933
#EXTINF:-1 tvg-id="TYC SPORTS HD" tvg-name="SPORTS: TYC SPORTS PLAY(PARTIDOS)" tvg-logo="https://img2.freepng.es/20180723/huc/kisspng-logo-tyc-sports-brand-trademark-mosaic-5b55e9fa8e43a0.5446456715323571145827.jpg" group-title="DEPORTES",SPORTS: TYC SPORTS PLAY(PARTIDOS)
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/53792
#EXTINF:-1 tvg-id="" tvg-name="SPORTS: TYC Sports(directo solo arg)" tvg-logo="https://statics-files.tycsports.com/frontend/tycsports/img/site_image.jpg" group-title="DEPORTES",SPORTS: TYC Sports(directo solo arg)
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/52688
#EXTINF:-1 tvg-id="TYC SPORTS HD" tvg-name="*SPORTS: HD:TYC SPORTS ARG FHD" tvg-logo="https://img2.freepng.es/20180723/huc/kisspng-logo-tyc-sports-brand-trademark-mosaic-5b55e9fa8e43a0.5446456715323571145827.jpg" group-title="DEPORTES",*SPORTS: HD:TYC SPORTS ARG FHD
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/108
#EXTINF:-1 tvg-id="TYC SPORTS HD" tvg-name="*SPORTS: SD: TYC SPORTS ARG SD" tvg-logo="https://img2.freepng.es/20180723/huc/kisspng-logo-tyc-sports-brand-trademark-mosaic-5b55e9fa8e43a0.5446456715323571145827.jpg" group-title="DEPORTES",*SPORTS: SD: TYC SPORTS ARG SD
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/34478
#EXTINF:-1 tvg-id="Canal TyC Sports" tvg-name="SPORTS: TYC Sport USA" tvg-logo="" group-title="DEPORTES",SPORTS: TYC Sport USA
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/20252
#EXTINF:-1 tvg-id="TNT SPORTS" tvg-name="SPORTS: FOX SPORTS 1 ARG FHD" tvg-logo="https://play.foxsportsla.com/assets/images/Logo-FS.png" group-title="DEPORTES",SPORTS: FOX SPORTS 1 ARG FHD
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/3668
#EXTINF:-1 tvg-id="FOX Sports" tvg-name="SPORTS SUR: Fox Sports 1 ARG HD" tvg-logo="http://zpapi.zetatv.com.uy/media/images/fox-sports.png" group-title="DEPORTES",SPORTS SUR: Fox Sports 1 ARG HD
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/41745
#EXTINF:-1 tvg-id="FOX Sports 2" tvg-name="SPORTS SUR: Fox Sports 2 ARG" tvg-logo="http://zpapi.zetatv.com.uy/media/images/fox-sports-2.png" group-title="DEPORTES",SPORTS SUR: Fox Sports 2 ARG
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/41746
#EXTINF:-1 tvg-id="" tvg-name="SPORTS:  ESPN EX  FOX SPORTS PREMIUM Op1" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/c/cf/Fox_Sports_Premium_Argentina_2020.png" group-title="DEPORTES",SPORTS:  ESPN EX  FOX SPORTS PREMIUM Op1
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/16521
#EXTINF:-1 tvg-id="TNT SPORTS" tvg-name="SPORTS: ESPN  EX Fox Sports Premium Op2" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/c/cf/Fox_Sports_Premium_Argentina_2020.png" group-title="DEPORTES",SPORTS: ESPN  EX Fox Sports Premium Op2
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/693
#EXTINF:-1 tvg-id="" tvg-name="SPORTS: ESPN EX  FOX SPORTS PREMIUM Op3 " tvg-logo="https://upload.wikimedia.org/wikipedia/commons/c/cf/Fox_Sports_Premium_Argentina_2020.png" group-title="ARGENTINA 1",SPORTS: ESPN EX  FOX SPORTS PREMIUM Op3 
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/16229
#EXTINF:-1 tvg-id="TNT SPORTS" tvg-name="SPORTS: HD:TNT SPORTS Op2" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/4/46/TNT_Sports_Logo_Vertical_%282017%29.png" group-title="DEPORTES",SPORTS: HD:TNT SPORTS Op2
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/99
#EXTINF:-1 tvg-id="TNT SPORTS" tvg-name="SPORTS: HD:TNT SPORTS Op3" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/4/46/TNT_Sports_Logo_Vertical_%282017%29.png" group-title="DEPORTES",SPORTS: HD:TNT SPORTS Op3
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/17095
#EXTINF:-1 tvg-id="TNT SPORTS" tvg-name="SPORTS: HD:TNT SPORTS Op4" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/4/46/TNT_Sports_Logo_Vertical_%282017%29.png" group-title="DEPORTES",SPORTS: HD:TNT SPORTS Op4
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/17096
#EXTINF:-1 tvg-id="ESPN" tvg-name="SPORTS: ESPN 1 SUR AR" tvg-logo="https://a1.espncdn.com/combiner/i?img=%2Fi%2Fespn%2Fespn_logos%2Fespn_red.png" group-title="DEPORTES",SPORTS: ESPN 1 SUR AR
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/41620
#EXTINF:-1 tvg-id="" tvg-name="SPORTS: ESPN 2 ARG" tvg-logo="http://elmasteriptv.com:8000/images/017f41a2ef4ff9d39f45f680b88cd23b.jpg" group-title="DEPORTES",SPORTS: ESPN 2 ARG
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/16663
#EXTINF:-1 tvg-id="TNT SPORTS" tvg-name="SPORTS: ESPN 1 ARG" tvg-logo="https://cdn.mitvstatic.com/channels/pe_espn_m.png" group-title="DEPORTES",SPORTS: ESPN 1 ARG
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/16662
#EXTINF:-1 tvg-id="" tvg-name="SPORTS: ESPN 2 ARG 2" tvg-logo="http://elmasteriptv.com:8000/images/017f41a2ef4ff9d39f45f680b88cd23b.jpg" group-title="DEPORTES",SPORTS: ESPN 2 ARG 2
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/31740
#EXTINF:-1 tvg-id="ESPN 2" tvg-name="SPORTS: ESPN 2 LINE ARG" tvg-logo="https://www.futbolenvivo.com.co/wp-content/uploads/2020/01/ESPN-2-en-vivo-online.jpg" group-title="DEPORTES",SPORTS: ESPN 2 LINE ARG
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/32157
#EXTINF:-1 tvg-id="" tvg-name="SPORTS: ESPN 3 ARG" tvg-logo="http://elmasteriptv.com:8000/images/021ee6585dd4256f549242057e972f41.png" group-title="DEPORTES",SPORTS: ESPN 3 ARG
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/16664
#EXTINF:-1 tvg-id="" tvg-name="SPORTS: ESPN 2 FHD" tvg-logo="http://www.cooprico.com.ar/images/historic/canales/espn2.png" group-title="DEPORTES",SPORTS: ESPN 2 FHD
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/31237
#EXTINF:-1 tvg-id="" tvg-name="SPORTS: Espn HD M" tvg-logo="http://elmasteriptv.com:8000/images/42fa21e42f99f88f0a881e12119ae313.jpg" group-title="DEPORTES",SPORTS: Espn HD M
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/17493
#EXTINF:-1 tvg-id="TNT SPORTS" tvg-name="SPORTS: ESPN + PLUS HD" tvg-logo="https://springboard-cdn.appadvice.com/wp-content/appadvice-v2-media/2018/02/espn-plus_dbc67d58aaa156a0ed06d06dd4972971-xl.jpg" group-title="DEPORTES",SPORTS: ESPN + PLUS HD
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/12157
#EXTINF:-1 tvg-id="" tvg-name="SPORTS: WIN SPORTS + PLUS COLOMBIA" tvg-logo="https://futbolete.com/wp-content/uploads/2019/12/capturadepantall-f0f54bcde7fc1471047f7b0e52fe8147-1200x600-1.jpg" group-title="DEPORTES",SPORTS: WIN SPORTS + PLUS COLOMBIA
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/16492
#EXTINF:-1 tvg-id="" tvg-name="Sports:Win Sport + 2" tvg-logo="https://futbolete.com/wp-content/uploads/2019/12/capturadepantall-f0f54bcde7fc1471047f7b0e52fe8147-1200x600-1.jpg" group-title="DEPORTES",Sports:Win Sport + 2
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/43501
#EXTINF:-1 tvg-id="Canal ESPN+ Latinoamérica" tvg-name="SPORTS: HD:ESPN +" tvg-logo="https://secure.espncdn.com/watchespn/images/espnplus/paywalls/ESPN_PLUS.logo@2x.png" group-title="DEPORTES",SPORTS: HD:ESPN +
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/4296
#EXTINF:-1 tvg-id="Canal ESPN Deportes" tvg-name="SPORTS: ESPN DEPORTES HD" tvg-logo="https://a1.espncdn.com/combiner/i?img=%2Fi%2Fespn%2Fespn_logos%2Fespndeportes_white.png" group-title="DEPORTES",SPORTS: ESPN DEPORTES HD
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/15490
#EXTINF:-1 tvg-id="Canal Fox Deportes" tvg-name="SPORTS: FOX DEPORTES HD" tvg-logo="https://is2-ssl.mzstatic.com/image/thumb/Purple123/v4/c3/f9/36/c3f936b0-4109-35e5-c22e-0ac53d9213f6/AppIcon-0-1x_U007emarketing-0-0-GLES2_U002c0-512MB-sRGB-0-0-0-85-220-0-0-0-10.png/1200x630wa.png" group-title="DEPORTES",SPORTS: FOX DEPORTES HD
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/15488
#EXTINF:-1 tvg-id="TNT SPORTS" tvg-name="SPORTS: Fox Sports 1 LA" tvg-logo="https://play.foxsportsla.com/assets/images/Logo-FS.png" group-title="DEPORTES",SPORTS: Fox Sports 1 LA
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/12311
#EXTINF:-1 tvg-id="" tvg-name="SPORTS: FOX SPORTS 1 SUR" tvg-logo="https://play.foxsportsla.com/assets/images/Logo-FS.png" group-title="DEPORTES",SPORTS: FOX SPORTS 1 SUR
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/12312
#EXTINF:-1 tvg-id="FOX Sports 3" tvg-name="*SPORTS: HD:FOX SPORTS 3" tvg-logo="https://static.wixstatic.com/media/0cd32b_36fc7a2ba14b4a81937ee99c0c5dd9f8.png" group-title="DEPORTES",*SPORTS: HD:FOX SPORTS 3
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/101
#EXTINF:-1 tvg-id="" tvg-name="Sports:DIRECTV SPORTS 1 ECUADOR" tvg-logo="" group-title="DEPORTES",Sports:DIRECTV SPORTS 1 ECUADOR
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/326
#EXTINF:-1 tvg-id="" tvg-name="SPORTS: TNT SPORT 1 CHILE" tvg-logo="http://1.bp.blogspot.com/-H0bRRXbMOwo/UhEC37cIzGI/AAAAAAAAOnU/plUJ7hWqclI/s1600/cdf+NUEVO.png" group-title="DEPORTES",SPORTS: TNT SPORT 1 CHILE
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/31268
#EXTINF:-1 tvg-id="" tvg-name="SPORTS_CL TNT SPORT 3 CHILE" tvg-logo="https://i.imgur.com/lEc55se.png" group-title="DEPORTES",SPORTS_CL TNT SPORT 3 CHILE
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/31270
#EXTINF:-1 tvg-id="" tvg-name="SPORTS_CL:  ESTADIO TNT SPORT CHILE" tvg-logo="https://vignette.wikia.nocookie.net/logopedia/images/f/fa/Logocdfpremium2019.png/revision/latest?cb=20190216005645" group-title="DEPORTES",SPORTS_CL:  ESTADIO TNT SPORT CHILE
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/31271
#EXTINF:-1 tvg-id="" tvg-name="SPORTS_CL TNT SPORT Premium CHILE" tvg-logo="https://i.imgur.com/lEc55se.png" group-title="DEPORTES",SPORTS_CL TNT SPORT Premium CHILE
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/31272
#EXTINF:-1 tvg-id="" tvg-name="SPORTS_CL TNT SPORT 1 CHILE" tvg-logo="https://cdn.mitvstatic.com/programs/cl_cdf-premium_p_m.jpg" group-title="DEPORTES",SPORTS_CL TNT SPORT 1 CHILE
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/31275
#EXTINF:-1 tvg-id="TNT SPORTS" tvg-name="*SPORTS: HD:GOLF CHANNEL" tvg-logo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTfDr5DY-PFDZnDKbK-nrOZ4eyYfLyfvfIUcWfFNNpqn0LwCLTw" group-title="DEPORTES",*SPORTS: HD:GOLF CHANNEL
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/107
#EXTINF:-1 tvg-id="" tvg-name="SPORTS: Bolivia Deportes" tvg-logo="http://directostv.teleame.com/wp-content/uploads/2018/02/bolivia-deportes.png" group-title="DEPORTES",SPORTS: Bolivia Deportes
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/387
#EXTINF:-1 tvg-id="" tvg-name="SPORTS: CDO BASICO CHILE" tvg-logo="http://directostv.teleame.com/wp-content/uploads/2018/06/cdo.png" group-title="DEPORTES",SPORTS: CDO BASICO CHILE
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/377
#EXTINF:-1 tvg-id="Canal Movistar Fórmula 1" tvg-name="SPORTS: F1 FHD" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/7/70/DAZN_F1_logo.png" group-title="DEPORTES",SPORTS: F1 FHD
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/211
#EXTINF:-1 tvg-id="" tvg-name="SPORTS: FUTV HD" tvg-logo="" group-title="DEPORTES",SPORTS: FUTV HD
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/19136
#EXTINF:-1 tvg-id="El Garage" tvg-name="SPORTS: GARAGE TV" tvg-logo="https://static.wixstatic.com/media/a6f875_c7ca84d7360f45ffb13d840b0649654e.png" group-title="DEPORTES",SPORTS: GARAGE TV
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/385
#EXTINF:-1 tvg-id="" tvg-name="SPORTS: MLB Live" tvg-logo="https://static1.squarespace.com/static/5bdfef0a697a98c05dd88ac0/5be3acea8985830adc1dc1f8/5c4fa2cc7ba7fc601bbd68c1/1548723770231/mlb.jpg?format=300w" group-title="DEPORTES",SPORTS: MLB Live
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/380
#EXTINF:-1 tvg-id="" tvg-name="SPORTS: MLB Network" tvg-logo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR8OvbTbRC3ih2o9AabgcJUPH6mXoGT232CfiMu78FDWmpIana8" group-title="DEPORTES",SPORTS: MLB Network
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/379
#EXTINF:-1 tvg-id="" tvg-name="SPORTS: Real Madrid TV" tvg-logo="https://media.cdnandroid.com/19/0b/92/cc/imagen-real-madrid-tv-0thumb.jpg" group-title="DEPORTES",SPORTS: Real Madrid TV
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/382
#EXTINF:-1 tvg-id="" tvg-name="SPORTS: Red Bull TV" tvg-logo="https://image.redbull.com/rbcom/010/2016-10-01/1331821221085_2/0010/1/1050/656/1/red-bull-tv.png" group-title="DEPORTES",SPORTS: Red Bull TV
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/381
#EXTINF:-1 tvg-id="" tvg-name="SPORTS: UFC NETWORK" tvg-logo="https://a.espncdn.com/combiner/i?img=/i/teamlogos/leagues/500/ufc.png" group-title="DEPORTES",SPORTS: UFC NETWORK
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/378
#EXTINF:-1 tvg-id="" tvg-name="SPORTS:TIGO PARAGUAY1" tvg-logo="" group-title="DEPORTES",SPORTS:TIGO PARAGUAY1
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/4230
#EXTINF:-1 tvg-id="" tvg-name="SPORTS:TIGO PARAGUAY2" tvg-logo="" group-title="DEPORTES",SPORTS:TIGO PARAGUAY2
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/4229
#EXTINF:-1 tvg-id="" tvg-name="SPORTS:TIGO SPORT CR 1" tvg-logo="" group-title="DEPORTES",SPORTS:TIGO SPORT CR 1
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/4235
#EXTINF:-1 tvg-id="" tvg-name="SPORTS:TIGO SPORTS 1 HD (BOLIVIA)" tvg-logo="" group-title="DEPORTES",SPORTS:TIGO SPORTS 1 HD (BOLIVIA)
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/4234
#EXTINF:-1 tvg-id="" tvg-name="SPORTS:TIGO SPORTS 2 HD (BOLIVIA)" tvg-logo="" group-title="DEPORTES",SPORTS:TIGO SPORTS 2 HD (BOLIVIA)
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/4232
#EXTINF:-1 tvg-id="" tvg-name="SPORTS:BE-IN,  LALIGA 1HD" tvg-logo="http://1.bp.blogspot.com/-4Wx5_LP1YJM/UjzhGIrKNlI/AAAAAAAACbI/4HmsX_hGkyg/s1600/imagSPORTS.jpg" group-title="DEPORTES 2",SPORTS:BE-IN,  LALIGA 1HD
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/31347
#EXTINF:-1 tvg-id="" tvg-name="SPORTS:BE IN,  SPORTS LA LIGA HD" tvg-logo="http://1.bp.blogspot.com/-4Wx5_LP1YJM/UjzhGIrKNlI/AAAAAAAACbI/4HmsX_hGkyg/s1600/imagSPORTS.jpg" group-title="DEPORTES 2",SPORTS:BE IN,  SPORTS LA LIGA HD
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/31348
#EXTINF:-1 tvg-id="" tvg-name="SPORTS arb: BE IN,  SPORTS 11 FHD" tvg-logo="http://1.bp.blogspot.com/-4Wx5_LP1YJM/UjzhGIrKNlI/AAAAAAAACbI/4HmsX_hGkyg/s1600/imagSPORTS.jpg" group-title="DEPORTES 2",SPORTS arb: BE IN,  SPORTS 11 FHD
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/31349
#EXTINF:-1 tvg-id="" tvg-name="SPORTS arb: BE IN,  SPORTS 10 FHD" tvg-logo="http://1.bp.blogspot.com/-4Wx5_LP1YJM/UjzhGIrKNlI/AAAAAAAACbI/4HmsX_hGkyg/s1600/imagSPORTS.jpg" group-title="DEPORTES 2",SPORTS arb: BE IN,  SPORTS 10 FHD
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/31350
#EXTINF:-1 tvg-id="" tvg-name="SPORTS arb: BE IN,  SPORTS 9 FHD" tvg-logo="http://1.bp.blogspot.com/-4Wx5_LP1YJM/UjzhGIrKNlI/AAAAAAAACbI/4HmsX_hGkyg/s1600/imagSPORTS.jpg" group-title="DEPORTES 2",SPORTS arb: BE IN,  SPORTS 9 FHD
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/31351
#EXTINF:-1 tvg-id="" tvg-name="SPORTS arb: BE IN,  SPORTS 8 FHD" tvg-logo="http://1.bp.blogspot.com/-4Wx5_LP1YJM/UjzhGIrKNlI/AAAAAAAACbI/4HmsX_hGkyg/s1600/imagSPORTS.jpg" group-title="DEPORTES 2",SPORTS arb: BE IN,  SPORTS 8 FHD
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/31352
#EXTINF:-1 tvg-id="" tvg-name="SPORTS arb: BE IN,  SPORTS 7 FHD" tvg-logo="http://1.bp.blogspot.com/-4Wx5_LP1YJM/UjzhGIrKNlI/AAAAAAAACbI/4HmsX_hGkyg/s1600/imagSPORTS.jpg" group-title="DEPORTES 2",SPORTS arb: BE IN,  SPORTS 7 FHD
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/31353
#EXTINF:-1 tvg-id="" tvg-name="SPORTS arb: BE IN,  SPORTS 5 FHD" tvg-logo="http://1.bp.blogspot.com/-4Wx5_LP1YJM/UjzhGIrKNlI/AAAAAAAACbI/4HmsX_hGkyg/s1600/imagSPORTS.jpg" group-title="DEPORTES 2",SPORTS arb: BE IN,  SPORTS 5 FHD
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/31354
#EXTINF:-1 tvg-id="" tvg-name="SPORTS arb: BE IN,  SPORTS 2 FHD" tvg-logo="http://1.bp.blogspot.com/-4Wx5_LP1YJM/UjzhGIrKNlI/AAAAAAAACbI/4HmsX_hGkyg/s1600/imagSPORTS.jpg" group-title="DEPORTES 2",SPORTS arb: BE IN,  SPORTS 2 FHD
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/31355
#EXTINF:-1 tvg-id="" tvg-name="SPORTS arb: BE IN,  SPORTS 1 FHD" tvg-logo="http://1.bp.blogspot.com/-4Wx5_LP1YJM/UjzhGIrKNlI/AAAAAAAACbI/4HmsX_hGkyg/s1600/imagSPORTS.jpg" group-title="DEPORTES 2",SPORTS arb: BE IN,  SPORTS 1 FHD
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/31356
#EXTINF:-1 tvg-id="" tvg-name="SPORTS arb: BE IN,  SPORTS 3 FHD" tvg-logo="http://1.bp.blogspot.com/-4Wx5_LP1YJM/UjzhGIrKNlI/AAAAAAAACbI/4HmsX_hGkyg/s1600/imagSPORTS.jpg" group-title="DEPORTES 2",SPORTS arb: BE IN,  SPORTS 3 FHD
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/31357
#EXTINF:-1 tvg-id="" tvg-name="SPORTS arb: BE IN,  SPORTS 4 FHD" tvg-logo="http://1.bp.blogspot.com/-4Wx5_LP1YJM/UjzhGIrKNlI/AAAAAAAACbI/4HmsX_hGkyg/s1600/imagSPORTS.jpg" group-title="DEPORTES 2",SPORTS arb: BE IN,  SPORTS 4 FHD
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/31358
#EXTINF:-1 tvg-id="" tvg-name="SPORTS arb: BE IN,  SPORTS 6 FHD" tvg-logo="http://1.bp.blogspot.com/-4Wx5_LP1YJM/UjzhGIrKNlI/AAAAAAAACbI/4HmsX_hGkyg/s1600/imagSPORTS.jpg" group-title="DEPORTES 2",SPORTS arb: BE IN,  SPORTS 6 FHD
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/31359
#EXTINF:-1 tvg-id="" tvg-name="SPORTS arb: BE IN,  SPORTS 12 FHD" tvg-logo="http://1.bp.blogspot.com/-4Wx5_LP1YJM/UjzhGIrKNlI/AAAAAAAACbI/4HmsX_hGkyg/s1600/imagSPORTS.jpg" group-title="DEPORTES 2",SPORTS arb: BE IN,  SPORTS 12 FHD
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/31360
#EXTINF:-1 tvg-id="" tvg-name="SPORTS us: BE IN,  SPORTS Ñ la liga " tvg-logo="http://1.bp.blogspot.com/-4Wx5_LP1YJM/UjzhGIrKNlI/AAAAAAAACbI/4HmsX_hGkyg/s1600/imagSPORTS.jpg" group-title="DEPORTES 2",SPORTS us: BE IN,  SPORTS Ñ la liga 
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/31362
#EXTINF:-1 tvg-id="" tvg-name="SPORTS:SK Y SPORTS 21" tvg-logo="https://www.thSPORTSun.co.uk/wp-content/uploads/2018/09/NINTCHDBPICT000353771160.jpg" group-title="DEPORTES 2",SPORTS:SK Y SPORTS 21
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/31365
#EXTINF:-1 tvg-id="" tvg-name="SPORTS:SK Y SPORTS 16" tvg-logo="https://www.thSPORTSun.co.uk/wp-content/uploads/2018/09/NINTCHDBPICT000353771160.jpg" group-title="DEPORTES 2",SPORTS:SK Y SPORTS 16
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/31366
#EXTINF:-1 tvg-id="" tvg-name="SPORTS: AYM Sports MEX" tvg-logo="http://elmasteriptv.com:8000/images/3f76d5d70b7fb3340973142ca42cc9f3.png" group-title="DEPORTES",SPORTS: AYM Sports MEX
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/17453
#EXTINF:-1 tvg-id="" tvg-name="SPORTS: DAZN" tvg-logo="https://queadslcontratar.com/sites/default/files/images/logos/dazn-200x300.png" group-title="DEPORTES",SPORTS: DAZN
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/40725
#EXTINF:-1 tvg-id="" tvg-name="ECU:El canal del Futbol" tvg-logo="https://www.xtrim.tv/images/xtr-vod-item-logo-ecdf.png" group-title="DEPORTES",ECU:El canal del Futbol
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/53975
#EXTINF:-1 tvg-id="" tvg-name="SPORTS: WIN SPORTS HD + PLUS COLOMBIA" tvg-logo="https://futbolete.com/wp-content/uploads/2019/12/capturadepantall-f0f54bcde7fc1471047f7b0e52fe8147-1200x600-1.jpg" group-title="DEPORTES",SPORTS: WIN SPORTS HD + PLUS COLOMBIA
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/58631
#EXTINF:-1 tvg-id="" tvg-name="SPORTS-ARG: TNT Sports" tvg-logo="" group-title="DEPORTES 2",SPORTS-ARG: TNT Sports
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/58930
#EXTINF:-1 tvg-id="" tvg-name="SPORTS-ARG: DIRECTV Sports Plus" tvg-logo="" group-title="DEPORTES 2",SPORTS-ARG: DIRECTV Sports Plus
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/58931
#EXTINF:-1 tvg-id="" tvg-name="SPORTS-ARG: DIRECTV Sports 2" tvg-logo="" group-title="DEPORTES 2",SPORTS-ARG: DIRECTV Sports 2
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/58932
#EXTINF:-1 tvg-id="" tvg-name="SPORTS-ARG: ESPN Argentina HD" tvg-logo="" group-title="DEPORTES 2",SPORTS-ARG: ESPN Argentina HD
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/58934
#EXTINF:-1 tvg-id="" tvg-name="SPORTS-ARG: ESPN 3 Sur HD" tvg-logo="" group-title="DEPORTES 2",SPORTS-ARG: ESPN 3 Sur HD
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/58935
#EXTINF:-1 tvg-id="" tvg-name="SPORTS-ARG: ESPN 2 Sur HD" tvg-logo="" group-title="DEPORTES 2",SPORTS-ARG: ESPN 2 Sur HD
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/58936
#EXTINF:-1 tvg-id="" tvg-name="SPORTS-ARG: ESPN Extra" tvg-logo="" group-title="DEPORTES 2",SPORTS-ARG: ESPN Extra
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/58937
#EXTINF:-1 tvg-id="" tvg-name="SPORTS-ARG: Fox Sports Premium" tvg-logo="" group-title="DEPORTES 2",SPORTS-ARG: Fox Sports Premium
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/58938
#EXTINF:-1 tvg-id="" tvg-name="SPORTS-ARG: Fox Sports Sur" tvg-logo="" group-title="DEPORTES 2",SPORTS-ARG: Fox Sports Sur
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/58939
#EXTINF:-1 tvg-id="" tvg-name="SPORTS-ARG: Fox Sports Sur 2" tvg-logo="" group-title="DEPORTES 2",SPORTS-ARG: Fox Sports Sur 2
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/58940
#EXTINF:-1 tvg-id="" tvg-name="SPORTS-ARG: Fox Sports 3 Sur" tvg-logo="" group-title="DEPORTES 2",SPORTS-ARG: Fox Sports 3 Sur
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/58941
#EXTINF:-1 tvg-id="" tvg-name="SPORTS-ARG: IVC Net HD" tvg-logo="" group-title="DEPORTES 2",SPORTS-ARG: IVC Net HD
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/58942
#EXTINF:-1 tvg-id="" tvg-name="SPORTS-ARG: DeporTV HD" tvg-logo="" group-title="DEPORTES 2",SPORTS-ARG: DeporTV HD
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/58943
#EXTINF:-1 tvg-id="" tvg-name="SPORTS-ARG: NBA TV International HD" tvg-logo="" group-title="DEPORTES 2",SPORTS-ARG: NBA TV International HD
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/58944
#EXTINF:-1 tvg-id="" tvg-name="SPORTS-ARG: Golf Channel" tvg-logo="" group-title="DEPORTES 2",SPORTS-ARG: Golf Channel
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/58945
#EXTINF:-1 tvg-id="" tvg-name="EVENTOS: TyC SPORT PLAY 1" tvg-logo="https://i.ibb.co/61yhwrb/2560px-Ty-C-Sports-play-1-logo-svg.png" group-title="EVENTOS",EVENTOS: TyC SPORT PLAY 1
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/70616
#EXTINF:-1 tvg-id="" tvg-name="EVENTOS: TyC SPORT PLAY 2" tvg-logo="https://i.ibb.co/z2mbPB5/2560px-Ty-C-Sports-play-2-logo-svg.png" group-title="EVENTOS",EVENTOS: TyC SPORT PLAY 2
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/70617
#EXTINF:-1 tvg-id="" tvg-name="EVENTOS: TyC SPORT PLAY 3" tvg-logo="https://i.ibb.co/7XmctpY/2560px-Ty-C-Sports-play-3-logo-svg.png" group-title="EVENTOS",EVENTOS: TyC SPORT PLAY 3
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/70618
#EXTINF:-1 tvg-id="" tvg-name="EVENTOS: TyC SPORT PLAY 4" tvg-logo="https://i.ibb.co/WWnWQ0V/2560px-Ty-C-Sports4-logo-svg.png" group-title="EVENTOS",EVENTOS: TyC SPORT PLAY 4
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/70619
#EXTINF:-1 tvg-id="" tvg-name="EVENTOS: TyC SPORT PLAY 5" tvg-logo="https://i.ibb.co/yP7hzk1/2560px-Ty-C-Sports5-logo-svg-1.png" group-title="EVENTOS",EVENTOS: TyC SPORT PLAY 5
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/70620
#EXTINF:-1 tvg-id="" tvg-name="EVENTOS: TyC SPORT PLAY 6" tvg-logo="https://i.ibb.co/jrdckjY/2560px-Ty-C-Sports6-logo-svg-2.png" group-title="EVENTOS",EVENTOS: TyC SPORT PLAY 6
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/70621
#EXTINF:-1 tvg-id="" tvg-name="EVENTOS: TyC SPORT PLAY 7" tvg-logo="https://i.ibb.co/f18yLZs/2560px-Ty-C-Sports7-logo-svg-3.png" group-title="EVENTOS",EVENTOS: TyC SPORT PLAY 7
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/70622
#EXTINF:-1 tvg-id="" tvg-name="EVENTOS: TyC SPORT PLAY 8" tvg-logo="https://i.ibb.co/Tv0xLW4/2560px-Ty-C-Sports8-logo-svg-4.png" group-title="EVENTOS",EVENTOS: TyC SPORT PLAY 8
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/70623
#EXTINF:-1 tvg-id="" tvg-name="EVENTOS: TyC SPORT PLAY 9" tvg-logo="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTlT9TyPbVEmRmTrv3cg-Ta5g_DDjs2N-F6Eg&usqp=CAU" group-title="EVENTOS",EVENTOS: TyC SPORT PLAY 9
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/70624
#EXTINF:-1 tvg-id="" tvg-name="EVENTOS: TyC SPORT PLAY 10" tvg-logo="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTlT9TyPbVEmRmTrv3cg-Ta5g_DDjs2N-F6Eg&usqp=CAU" group-title="EVENTOS",EVENTOS: TyC SPORT PLAY 10
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/70625
#EXTINF:-1 tvg-id="" tvg-name="EVENTOS: TNT Sports Brasil" tvg-logo="https://upload.wikimedia.org/wikipedia/pt/d/dc/Logotipo_TNT_Sports.png" group-title="EVENTOS",EVENTOS: TNT Sports Brasil
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/70626
#EXTINF:-1 tvg-id="" tvg-name="EVENTOS: TNT Sports 2 Brasil" tvg-logo="https://upload.wikimedia.org/wikipedia/pt/d/dc/Logotipo_TNT_Sports.png" group-title="EVENTOS",EVENTOS: TNT Sports 2 Brasil
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/70627
#EXTINF:-1 tvg-id="" tvg-name="EVENTOS: TNT Sports 4 Brasil" tvg-logo="https://upload.wikimedia.org/wikipedia/pt/d/dc/Logotipo_TNT_Sports.png" group-title="EVENTOS",EVENTOS: TNT Sports 4 Brasil
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/70628
#EXTINF:-1 tvg-id="" tvg-name="EVENTOS: F1FULLHFD" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/7/70/DAZN_F1_logo.png" group-title="EVENTOS",EVENTOS: F1FULLHFD
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/70795


#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="https://www.portalpopcyber.com/wp-content/uploads/2021/10/mtv-logo-952x630.png",MTV LATINOAMERICA
https://edge2-ccast-sl.cvattv.com.ar/live/c6eds/MTV_HD/SA_SAGEMCOM/MTV_HD.m3u8
#EXTINF:-1  tvg-id="El Trece" group-title="Argentina" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/4/45/Eltrece_logotipo_2018.png",El Trece
https://edge2-ccast-sl.cvattv.com.ar/live/c3eds/ArtearHD/SA_SAGEMCOM/ArtearHD.m3u8
#EXTINF:-1  tvg-id="El Trece" group-title="Argentina" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/4/45/Eltrece_logotipo_2018.png",El Trece 2
http://181.30.129.66:80/live/live2/ArtearHD/SA_Live_fta/ArtearHD.m3u8

#EXTINF:-1  tvg-id="El Trece" group-title="Argentina" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/4/45/Eltrece_logotipo_2018.png",El Trece 3
https://live-01-02-eltrece.vodgc.net/eltrecetv/tracks-v1a1/mono.m3u8


#EXTINF:-1  tvg-id="El Trece" group-title="Argentina" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/4/45/Eltrece_logotipo_2018.png",El Trece 4
https://raw.githubusercontent.com/fgillusi/IPTV-Argentina/main/ArtearHD.m3u8

#EXTINF:-1  tvg-id="El Trece" group-title="Argentina" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/4/45/Eltrece_logotipo_2018.png",El Trece 5
http://jumangis.com:2082/Sv503iptv22/QR7E5sm3J2/95534



#EXTINF:-1  tvg-id="El Trece" group-title="Argentina" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/4/45/Eltrece_logotipo_2018.png", EL TRECE INTERNACIONAL
http://jumangis.com:2082/Sv503iptv22/QR7E5sm3J2/95506

#EXTINF:-1 tvg-logo="https://i.imgur.com/srtddlN.png" group-title="Argentina",TV Publica
https://delivery.cdn.rcs.net.ar/mnp/tvp/output.mpd

#EXTINF:-1 tvg-logo="https://i.imgur.com/IS4LViL.png" group-title="Argentina",El Nueve
https://delivery.cdn.rcs.net.ar/mnp/elnueve/output.mpd








#EXTINF:-1 group-title="Argentina" tvg-logo="https://yt3.ggpht.com/ytc/AKedOLSYU51c8SbrkWZeNBRMFeCnGv0YXPpXuEGBNq-X5g=s88-c-k-c0x00ffffff-no-rj",Encuentro
https://raw.githubusercontent.com/fgillusi/IPTV-Argentina/main/Encuentro.m3u8


#EXTINF:-1, tvg-id="Telefe" group-title="Argentina" tvg-name="Telefe" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Telefe_Logo.svg/1280px-Telefe_Logo.svg.png",Telefe
http://titanlivetv.com:8080/8cEW8XH37tDT/GP4qLxWhcCkd/111675

#EXTINF:-1, tvg-id="Telefe" group-title="Argentina" tvg-name="Telefe" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Telefe_Logo.svg/1280px-Telefe_Logo.svg.png",Telefe
https://edge2-ccast-sl.cvattv.com.ar/live/c3eds/TelefeHD/SA_SAGEMCOM/TelefeHD.m3u8



#EXTINF:-1 tvg-id="Telefe" tvg-name="Telefe" group-title="Argentina" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Telefe_Logo.svg/1280px-Telefe_Logo.svg.png",TELEFE 2
https://raw.githubusercontent.com/fgillusi/IPTV-Argentina/main/TelefeHD.m3u8
#EXTINF:-1 tvg-id="Telefe" tvg-name="Telefe" group-title="Argentina" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Telefe_Logo.svg/1280px-Telefe_Logo.svg.png",TELEFE 3
https://raw.githubusercontent.com/fgillusi/IPTV-Argentina/main/TelefeHD-edge9.m3u8
#EXTINF:-1 tvg-id="Telefe" tvg-name="Telefe" group-title="Argentina" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Telefe_Logo.svg/1280px-Telefe_Logo.svg.png",TELEFE 4
http://jumangis.com:2082/Sv503iptv22/QR7E5sm3J2/95508
#EXTINF:-1 tvg-id="Telefe" tvg-name="Telefe" group-title="Argentina" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Telefe_Logo.svg/1280px-Telefe_Logo.svg.png",TELEFE 5
https://delivery.cdn.rcs.net.ar/mnp/telefe/output.mpd

#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",América TV
https://edge2-ccast-sl.cvattv.com.ar/live/c3eds/AmericaTV/SA_SAGEMCOM/AmericaTV.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",IP - Información Periodística
https://octubre-live.cdn.vustreams.com/live/ip/live.isml/live-audio_1=128000-video=2800000.m3u8

#EXTINF:-1 group-title="Argentina",el siete (tv publica)
https://raw.githubusercontent.com/fgillusi/IPTV-Argentina/main/Canal7.m3u8

#EXTINF:-1 group-title="Argentina",EL NUEVE HD
https://raw.githubusercontent.com/fgillusi/IPTV-Argentina/main/Canal9.m3u8

#EXTINF:-1 group-title="Argentina",encuentro
https://5fb24b460df87.streamlock.net/live-cont.ar/encuentro/playlist.m3u8

#EXTINF:-1 group-title="Argentina" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/Informaci%C3%B3n_Period%C3%ADstica_IP_Logo.svg/260px-Informaci%C3%B3n_Period%C3%ADstica_IP_Logo.svg.png" group-title="NOTICIAS", IP  24.5         
https://d1nmqgphjn0y4.cloudfront.net/live/ip/live.isml/live-audio_1=128000-video=4499968.m3u8

#EXTINF:-1 group-title="Argentina" tvg-logo="http://www.grupocronica.com.ar/mediakit/wp-content/uploads/2017/10/cronica-hd-con-sombra-grande.png" , CRONICA HD  24.4
https://g5.vxral-slo.transport.edge-access.net/b10/ngrp:cronicatv_video1-100044_all/cronicatv_video1-100044_720p/index.m3u8

#EXTINF:-1 group-title="Argentina" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/LogoCanal26.png/120px-LogoCanal26.png" , CANAL 26  24.2
http://live-edge01.telecentro.net.ar/live/smil:c26.smil/chunklist_w794690609_b2628000_sleng.m3u8

#EXTINF:-1 group-title="Argentina" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/A24_%282019-1%29.png/150px-A24_%282019-1%29.png" , A24  36.3
https://g1.vxral-hor.transport.edge-access.net/a15/ngrp:a24-100056_all/a24-100056_720p.m3u8



#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/c/c8/Am%C3%A9rica_TV_%28Nuevo_logo_Junio_2020%29.png" group-title="Argentina", AMERICA HD  36.1
https://prepublish.f.qaotic.net/a07/americahls-100056/playlist_720p.m3u8

#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/b/b0/Canal9.jpg" group-title="Argentina", CANAL 9  35.1 
https://ar-elnueve-elnueve-live.ned.media/live.m3u8?iut=eyJwYXJhbXMiOnsiZXhwIjoxNjI5NDY0OTI5LCJzZXNzaW9uIjoiMTgxLjQ0LjEyOS43MSIsIndoaXRlbGlzdCI6WyIxODEuNDQuMTI5LjcxIl19LCJzaWduYXR1cmUiOiJjNzQ2NTZjMjM0MjI5MmYwMDBhMzExZjNlYWIzMzBlNzVmYjJmNzY1In0=



#EXTINF:-1 tvg-logo="http://images.pluto.tv/channels/5f523aa5523ae000074745ec/colorLogoPNG.png" group-title="NOTICIAS", TELEFÉ NOTICIAS
http://service-stitcher.clusters.pluto.tv/stitch/hls/channel/5f523aa5523ae000074745ec/master.m3u8?advertisingId=&appName=web&appVersion=unknown&appStoreUrl=&architecture=&buildVersion=&clientTime=0&deviceDNT=0&deviceId=bff334c2-6307-11eb-b3fa-019cb96f121b&deviceMake=Chrome&deviceModel=web&deviceType=web&deviceVersion=unknown&includeExtendedEvents=false&sid=dffc36b9-57c6-4973-9903-2f83d465ac40&userId=&serverSideAds=true

#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/8/8f/Canal13_logo.png" group-title="Argentina", CANAL 13  33.1
http://edge5-sl.cvattv.com.ar/live/c3eds/ArtearHD/SA_SAGEMCOM/ArtearHD-avc1_379968=10016.m3u8



#EXTINF:-1 tvg-logo="https://scontent.fepa11-1.fna.fbcdn.net/v/t1.6435-9/206638151_10223169123710059_3666810289391430657_n.jpg?_nc_cat=101&ccb=1-3&_nc_sid=825194&_nc_eui2=AeGxugJ54qa7RhgKBnLTrHOu14OonvQq8lrXg6ie9CryWkCQzaYyrufVmZGkiprZVM0&_nc_ohc=dbLCQPiMFxEAX9X0jrT&_nc_ht=scontent.fepa11-1.fna&oh=afeef92e5377cb7720df7b2f4afc60c8&oe=6127F95F" group-title="Argentina", SSIPTV ARG TV
http://service-stitcher.clusters.pluto.tv/stitch/hls/channel/5df265697ec3510009df1ef0/master.m3u8?advertisingId=&appName=web&appVersion=unknown&appStoreUrl=&architecture=&buildVersion=&clientTime=0&deviceDNT=0&deviceId=bff1d530-6307-11eb-b3fa-019cb96f121b&deviceMake=Chrome&deviceModel=web&deviceType=web&deviceVersion=unknown&includeExtendedEvents=false&sid=ec2383fd-6e28-4df5-9d1c-b66eee700e0c&userId=&serverSideAds=true

#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Net_TV_logo.png/120px-Net_TV_logo.png" group-title="Argentina", NET TV  27.2
https://unlimited1-us.dps.live/nettv/nettv.smil/nettv/livestream1/playlist.m3u8

#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Paka-paka.svg/245px-Paka-paka.svg.png" group-title="Argentina", PAKA PAKA  22.2
https://5fb24b460df87.streamlock.net/live-cont.ar/pakapaka/playlist.m3u8

#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Logo_The_Simpsons.svg/1200px-Logo_The_Simpsons.svg.png" group-title="Argentina", LOS SIMPSONS
https://videostreaming.cloudserverlatam.com/cloudservertv/cloudservertv/playlist.m3u8

#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/d/d6/Logomagic96.png" group-title="Argentina", MAGIC KIDS
https://live.admefy.com/live/clean_peach_ef224.m3u8

#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Cine.Ar_logo.svg/1280px-Cine.Ar_logo.svg.png" group-title="Argentina", CINEAR  22.4
https://5fb24b460df87.streamlock.net/live-cont.ar/cinear/playlist.m3u8   

#EXTINF:-1 tvg-logo="http://images.pluto.tv/channels/5de91cf02fc07c0009910465/colorLogoPNG.png" group-title="Argentina", TELEFÉ CLÁSICO
http://service-stitcher.clusters.pluto.tv/stitch/hls/channel/5de91cf02fc07c0009910465/master.m3u8?advertisingId=&appName=web&appVersion=unknown&appStoreUrl=&architecture=&buildVersion=&clientTime=0&deviceDNT=0&deviceId=bff1ae23-6307-11eb-b3fa-019cb96f121b&deviceMake=Chrome&deviceModel=web&deviceType=web&deviceVersion=unknown&includeExtendedEvents=false&sid=a367d0d9-b23d-4bb5-8d48-55f0cbeac4fb&userId=&serverSideAds=true

#EXTINF:-1 tvg-logo="https://lh3.googleusercontent.com/gwVNQhVICXN4Q7djaLyeQGCiMAa4Jum_PqeVaFZ1W90T4Y0G297wC1upnHRcKUbA6Q=w412-h220-rw" group-title="Argentina", GEN TV  17.3
https://videohd.live:19360/8010/8010.m3u8

#EXTINF:-1 tvg-logo="https://lh3.googleusercontent.com/-Od4eldPqILM/XjtCKHxeYSI/AAAAAAAAvok/HDnuaXs9cCsFzbr0QrQtw3bYeDB0_5osACK8BGAsYHg/s0/2020-02-05.png" group-title="Argentina", CINCO TV TIGRE  30.1
https://59537faa0729a.streamlock.net/cincotv/cincotv/playlist.m3u8

#EXTINF:-1 tvg-logo="https://neotvdigital.com.ar/imagenes/logo1.png" group-title="Argentina", NEO TV DIGITAL  14.1
https://videostream.shockmedia.com.ar:19360/neotvdigital/neotvdigital.m3u8

#EXTINF:-1 tvg-logo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRMm0MM0BtkhB9xHWsECtnky05aGfA8KKnDSg&usqp=CAU" group-title="Argentina", CANAL 29 QUILMES 18.1
http://inliveserver.com:1935/8386/8386/playlist.m3u8

#EXTINF:-1 tvg-logo="https://serenotv.com/wp-content/uploads/2020/08/canal-telecreativa.jpg" group-title="Argentina", TELECREATIVA LANUS
https://panel.dattalive.com/8012/8012/playlist.m3u8

#EXTINF:-1 tvg-logo="https://image.winudf.com/v2/image1/Y29tLmExMjNmcmVlYXBwcy5mcmVlLmFwcDVkNWVjMWY4ODliOThfaWNvbl8xNTY3NjE5OTcxXzAxNw/icon.png?w=170&fakeurl=1" group-title="Argentina", CANAL 4 TELEAIRE SAN MARTIN
https://stmvideo2.livecastv.com/canal4/canal4/playlist.m3u8

#EXTINF:-1 tvg-logo="https://lh3.googleusercontent.com/-SlqJrd0GiYk/XjtCBz2FbhI/AAAAAAAAvog/HkkKzNWrEOYiE08Rdlw-mxsDtzpJ_zD8wCK8BGAsYHg/s0/2020-02-05.png" group-title="Argentina", CANAL 6 MORENO
https://5975e06a1f292.streamlock.net:4443/canal6moreno/canal6moreno/playlist.m3u8

#EXTINF:-1 tvg-logo="http://www.radiosargentina.com.ar/png/VIC2PROV.png" group-title="Argentina", PROVINCIAL TV
http://www.trimi.com.ar/provincial/streaming/mystreamProvincialHSMed.m3u8

#EXTINF:-1 tvg-logo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRG3riJIJamJMTaIwOIMuqH2cdOfdLQIyz9-NHeJ-pF2tQJsM-akUEu5MuYVspASJxZNQ&usqp=CAU" group-title="Argentina", CIUDAD MAGAZINE
https://g4.mc-slo.transport.edge-access.net/a09/ngrp:magazine_live01-100083_all/magazine_live01-100083_720p.m3u8

#EXTINF:-1 tvg-logo="http://www.canalkzo.com/images/lg_kzo.svg" group-title="Argentina", KZO
http://g2.vxral-slo.transport.edge-access.net/nx-beta/nx.hor.livetx.01/5eaa642772b3a25e2c28699e_540p/index.m3u8



#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/e/eb/TYC_SPORTS.jpg/800px-TYC_SPORTS.jpg" group-title="Argentina", TyC SPORT 
https://d3055hobuue3je.cloudfront.net/out/v1/b841c366cbe540e6a106c3ba83e5c8d6/index.m3u8

#EXTINF:-1 tvg-logo="https://i.ibb.co/NTNvh66/header-ciudadmagica.jpg" group-title="DEPORTE", CIUDAD MAGICA TV
https://srv2.zcast.com.br/ciudadm/ciudadm/playlist.m3u8


#EXTINF:-1 tvg-logo="https://lh3.googleusercontent.com/-2gN4wEv_qPI/XjtKDwMuIQI/AAAAAAAAvrY/VTtJwZALBykDRnM8ia0Xbqi0FbREvdrZACK8BGAsYHg/s0/2020-02-05.png" group-title="Argentina", GARAGE TV
http://186.0.233.76:1935/Garage/smil:garage.smil/chunklist_w2049053275_b1296000_sleng.m3u8

#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Deutsche_Welle_symbol_2012.svg/150px-Deutsche_Welle_symbol_2012.svg.png" group-title="NOTICIAS", DW ESPAÑOL
https://dwamdstream104.akamaized.net/hls/live/2015530/dwstream104/stream05/streamPlaylist.m3u8

#EXTINF:-1 tvg-logo="http://tvabierta.weebly.com/uploads/5/1/3/4/51344345/mirador.png" group-title="Argentina", MIRADOR  22.3
https://5fb24b460df87.streamlock.net/live-cont.ar/mirador/playlist.m3u8 

#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/4/4c/Telemax.png" group-title="Argentina", TELEMAX  26.3
https://live-edge01.telecentro.net.ar/live/smil:tlx.smil/playlist.m3u8

#EXTINF:-1 tvg-logo="https://d2ucqd3jt48qxz.cloudfront.net/img/footer-logo.png" group-title="Argentina", ORBE 21  21.2
https://cdn2.zencast.tv:30443/orbe/orbe21smil/playlist.m3u8

#EXTINF:-1 tvg-logo="https://dz92jh1unkapm.cloudfront.net/accounts/5cf95117cb97cae8e2c36676/logo.png" group-title="Argentina", UNIFE TV  25.1
https://dacastmmd.mmdlive.lldns.net/dacastmmd/98adedd6dec04a2d8663899b927f9383/chunklist_b4628000.m3u8

#EXTINF:-1 tvg-logo="http://www.radiosargentina.com.ar/png/VISANTAM.png" group-title="Argentina", SANTA MARIA
http://www.trimi.com.ar/santa_maria/streaming/mystreamSantaMariaHSMed.m3u8



#EXTINF:-1 tvg-logo="http://www.tectv.gob.ar/resources/img/logo.png" group-title="Argentina", TEC TV  22.5
https://g3.mc-hor.transport.edge-access.net/a09/ngrp:gcba_video3-100042_all/gcba_video3-100042_720p.m3u8






#EXTINF:-1, CANAL 26 
http://200.115.193.177/live/26hd-720/.m3u8

#EXTM3U x-tvg-url="https://iptv-org.github.io/epg/guides/ar/mi.tv.epg.xml"


#EXTM3U



#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Telefe Rosario (720p) [Not 24/7]
http://telefewhitehls-lh.akamaihd.net/i/whitelist_hls@302302/master.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Telefe Santa F  (720p) [Not 24/7]
https://tlfcapitalhls-lh.akamaihd.net/i/canal13santafe_1@751190/master.m3u8?hdnea=st=1645561118~exp=1645737518~acl=/i/canal13santafe_1@751190/*~hmac=5c257cbcbcb2730ac5fedbdd6ee12ad256104b441711d394397744f94a404ad2
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Telefe Mar del Plata (720p) [Not 24/7]
https://tlfcapitalhls-lh.akamaihd.net/i/mdqdistri02_1@829747/master.m3u8?hdnea=st=1645560795~exp=1645737195~acl=/i/mdqdistri02_1@829747/*~hmac=95846b50cc71a3e1a7ca5f4eeec6f4837bf26e61c71ec58e542546b4a2b63a3e
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Telefe Tucuman (720p) [Not 24/7]
https://tlfcapitalhls-lh.akamaihd.net/i/canal8tucuman_1@787002/master.m3u8?hdnea=st=1645561206~exp=1645737606~acl=/i/canal8tucuman_1@787002/*~hmac=0c32d04d2d681e86b55f0dc4afc66b9a7ea33784ebaf36fe1a1e2078b191f94c







#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal 26  (San Justo-Arg.)
http://200.115.193.177/live/26hd-720/.m3u8?CompartilhandoIPTV
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal 26  (San Justo-Arg.)
http://live-edge01.telecentro.net.ar:1935/live/26hd-720/livestream.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal 26  (San Justo-Arg.)
http://live-edge01.telecentro.net.ar/live/26hd-720/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal 26 (San Justo-Arg.)
http://live-edge01.telecentro.net.ar/live/smil:c26.smil/chunklist_w858131162_b414000_sleng.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://panel.dattalive.com:1935/8250/8250/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://uni5rtmp.tulix.tv:1935/bettervida/bettervida/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://moiptvhls-i.akamaihd.net/hls/live/652315/secure/master.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://api.new.livestream.com/accounts/22636012/events/8242619/live.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://www.coninfo.net:1935/tvcinco/live1/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://g1.vxral-hor.transport.edge-access.net/a15/ngrp:a24-100056_all/a24-100056.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://inliveserver.com:1936/15506/15506/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://azxtv.com/hls/stream.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://186.0.233.76:1935/Argentinisima/smil:argentinisima.smil/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://vs-hls-push-uk-live.akamaized.net/x=3/i=urn:bbc:pips:service:bbc_news_channel_hd/mobile_wifi_main_sd_abr_v2.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://103.199.161.254/Content/bbcworld/Live/Channel(BBCworld)/index.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://45.5.8.78:8000/play/a00i
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://api.new.livestream.com/accounts/679322/events/3782013/live.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://59d52c5a5ce5e.streamlock.net:4443/canal3rosario/ngrp:canal3rosario_all/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://190.52.32.13:1935/canal4/smil:manifest.smil/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://live.canalnueve.tv/canal.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://5b3050bb1b2d8.streamlock.net/viviloendirecto2/canal9/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://cdn2.zencast.tv:30443/live/canal10smil/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://panel.dattalive.com:1935/8204/8204/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://stmv4.questreaming.com/fenixlarioja/fenixlarioja/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://5f700d5b2c46f.streamlock.net/madryntv/madryntv/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://arcast.net:1935/mp/mp/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://200.115.193.177/live/26hd-720/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://www.trimi.com.ar/provincial/streaming/mystream.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://5e7cdf2370883.streamlock.net/tdconline/tdconline/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://panel.dattalive.com/8250/8250/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://5f700d5b2c46f.streamlock.net/catamarcatelevision/catamarcatelevision/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://s8.stweb.tv/chacra/live/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://59537faa0729a.streamlock.net/cincotv/cincotv/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://5fb24b460df87.streamlock.net/live-cont.ar/cinear/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://coninfo.net:1935/chacodxdtv/live/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://dwamdstream102.akamaized.net/hls/live/2015525/dwstream102/index.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://dwamdstream104.akamaized.net/hls/live/2015530/dwstream104/index.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://186.0.233.76:1935/Garage/smil:garage.smil/master.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://elonceovh.elonce.com/hls/live.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://v4.tustreaming.cl/enlacebpbtv/index.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://euronews-euronews-spanish-2-mx.samsung.wurl.com/manifest/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://f24hls-i.akamaihd.net/hls/live/221147/F24_EN_HI_HLS/master.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://f24hls-i.akamaihd.net/hls/live/520845/F24_ES_HI_HLS/master.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://d1nmqgphjn0y4.cloudfront.net/live/ip/live.isml/5ee6e167-1167-4a85-9d8d-e08a3f55cff3.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://srv1.zcast.com.br/lavozdetucuman/lavozdetucuman/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://videostreaming.cloudserverlatam.com/8066/8066/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://panel.dattalive.com:1935/8250/8250/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://live-edge01.telecentro.net.ar/live/smil:musictop.smil/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://unlimited1-us.dps.live/nettv/nettv.smil/nettv/livestream1/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://stream.live.novotempo.com/tv/smil:tvnuevotiempo.smil/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://mdstrm.com/live-stream-playlist/5b9076d18ef7b22560354649.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://wowza.telpin.com.ar:1935/live-powerTV/power.stream/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://rbmn-live.akamaized.net/hls/live/590964/BoRB-AT/master.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://strm.yandex.ru/kal/rt_hd/rt_hd0.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://www.trimi.com.ar/santa_maria/streaming/mystream.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://panel.seo.tv.bo:3337/live/franzbalboa2live.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://paneltv.online:1936/8116/8116/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://tastemade-es8intl-roku.amagi.tv/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://telefewhitehls-lh.akamaihd.net/i/whitelist_hls@302302/master.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://videostream.shockmedia.com.ar:1936/telejunin/telejunin/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://live-edge01.telecentro.net.ar/live/smil:tlx.smil/master.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://www.coninfo.net:1935/previsoratv/live/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://cnnsanjuan.com:9999/live/telesol/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://wowza.telpin.com.ar:1935/telpintv/smil:ttv.stream.smil/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://wowza.telpin.com.ar:1935/telpintv/ttv.stream/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://v4.tustreaming.cl/tevexinter/index.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://live-edge01.telecentro.net.ar/live/smil:trm.smil/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://tv-trtworld.live.trt.com.tr/master.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://streamspub.manasat.com:1935/tvar/tvmanaar2/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://cdnh4.iblups.com/hls/irtp.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://america-crtvg.flumotion.com/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://stratus.stream.cespi.unlp.edu.ar/hls/tvunlp.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://59a564764e2b6.streamlock.net/vallenato/Vallenato2/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://5f700d5b2c46f.streamlock.net/vertv/vertv/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://186.0.233.76:1935/Garage/garage.smil/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Garage TV (Argentina)
http://186.0.233.76:1935/Garage/smil:garage.smil/master.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Garage TV  (Argentina)
http://186.0.233.76:1935/Garage/smil:garage.smil/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Garage TV  (Argentina)
http://186.0.233.76:1935/Garage/smil:garage.smil/chunklist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Music Top  (Argentina)
http://live-edge01.telecentro.net.ar/live/smil:musictop.smil/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Telemax  HD Argent.
http://live-edge01.telecentro.net.ar/live/smil:tlx.smil/chunklist_w950122583_b1828000_sleng.m3u8

#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",TV Man  Argentina (576p) [Not 24/7]
http://streamspub.manasat.com:1935/tvar/tvmanaar2/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",24/7 Canal de Noticias
http://59c5c86e10038.streamlock.net:1935/6605140/6605140/playlist.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",5RTV Santa Fe
http://api.new.livestream.com/accounts/22636012/events/8242619/live.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",5TV (Corrientes) (480p)
http://www.coninfo.net:1935/tvcinco/live1/playlist.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",5TV Corrientes
http://www.coninfo.net:1935/tvcinco/live1/chunklist_w1546509083.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",CANAL PROVINCIAL SAN MIGUEL
http://www.trimi.com.ar/provincial/streaming/mystream.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal 26
http://200.115.193.177/live/26hd-180/playlist.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal 26
http://200.115.193.177/live/26hd-720/.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal 26
http://200.115.193.177/live/26hd-720/playlist.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal 26
http://live-edge01.telecentro.net.ar/live/26hd-360/playlist.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal 26
http://live-edge01.telecentro.net.ar/live/26hd-720/playlist.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal 26
http://live-edge01.telecentro.net.ar/live/smil:c26.smil/playlist.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal 26
http://live-edge01.telecentro.net.ar:1935/live/26hd-720/livestream.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Chacra TV
http://s8.stweb.tv:1935/chacra/live/chunks.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Ciudad TV Chaco
http://coninfo.net:1935/chacodxdtv/live/chunklist_w1251301598.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Music Top
http://live-edge01.telecentro.net.ar/live/smil:musictop.smil/playlist.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Music TOP
http://live-edge01.telecentro.net.ar/live/smil:musictop.smil/chunklist_w1582140541_b364000_sleng.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Music Top
http://live-edge01.telecentro.net.ar/live/msctphd-720/playlist.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Music Top
http://live-edge01.telecentro.net.ar/live/musictop.smil/.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Music Top
http://live-edge01.telecentro.net.ar/live/smil:musictop.smil/chunklist_w538311571_b364000_sleng.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Music Top
http://live-edge01.telecentro.net.ar:1935/live/msctphd-720/playlist.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",TLX
http://live-edge01.telecentro.net.ar/live/tlxhd-720/master.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",TLX
http://live-edge01.telecentro.net.ar/live/smil:tlx.smil/master.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",TV Man  C rdoba
http://csvl03.manasat.com:1935/tvar/tvmanaar2/playlist.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",TV Man  C rdoba
http://streamspub.manasat.com:1935/tvar/tvmanaar2/playlist.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Telefe Rosario (720p)
http://telefewhitehls-lh.akamaihd.net/i/whitelist_hls@302302/master.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Telemax
http://live-edge01.telecentro.net.ar/live/tlxhd-720/playlist.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",1HD Music
http://1hdru-hls-otcnet.cdnvideo.ru/onehdmusic/mono.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Latino Kids TV * | UY
https://videostreaming.cloudserverlatam.com/8066/8066/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="269" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/269_Canal_13_San_Luis.png",tvg-id="269" tvg-name="Canal 13 San Luis" tvg-logo="https://www.m3u.cl/logo/269_Canal_13_San_Luis.png,  Canal 13 San Luis * | AR
https://5975e06a1f292.streamlock.net:4443/sanluistv/ngrp:sanluistv_all/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="277" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/277_Canal_XFN.png",tvg-id="277" tvg-name="Canal XFN" tvg-logo="https://www.m3u.cl/logo/277_Canal_XFN.png,  Canal XFN * | AR
https://streamconex.com:1936/canalxfn/canalxfn/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="218" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/218_Senal_Urbana.png",tvg-id="218" tvg-name="Se al Urbana" tvg-logo="https://www.m3u.cl/logo/218_Senal_Urbana.png,  Se al Urbana * | AR
https://stmvideo2.livecastv.com/urbana98/urbana98/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="1026" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/1026_Tele_Mix.png",tvg-id="1026" tvg-name="Tele Mix" tvg-logo="https://www.m3u.cl/logo/1026_Tele_Mix.png,  Tele Mix * | AR
https://panel.dattalive.com:443/8068/8068/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="1010" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/1010_UNaM_Transmedia.png",tvg-id="1010" tvg-name="UNaM Transmedia" tvg-logo="https://www.m3u.cl/logo/1010_UNaM_Transmedia.png,  UNaM Transmedia * | AR
http://192.100.186.53:8090/hls/live.stream.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="488" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/488_Anime_Zone_TV.png",tvg-id="488" tvg-name="Anime Zone TV" tvg-logo="https://www.m3u.cl/logo/488_Anime_Zone_TV.png,  Anime Zone TV | AR
http://azxtv.com/hls/stream.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="206" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/206_Paka_Paka.jpg",tvg-id="206" tvg-name="Paka Paka" tvg-logo="https://www.m3u.cl/logo/206_Paka_Paka.jpg,  Paka Paka | AR
https://5fb24b460df87.streamlock.net/live-cont.ar/pakapaka/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="251" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/251_13_Max_Television.png",tvg-id="251" tvg-name="13 Max Television" tvg-logo="https://www.m3u.cl/logo/251_13_Max_Television.png,  13 Max Television | AR
http://coninfo.net:1935/13maxhd/live13maxtvnuevo_720p/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="221" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/221_5R_TV_Santa_Fe.png",tvg-id="221" tvg-name="5R TV Santa Fe" tvg-logo="https://www.m3u.cl/logo/221_5R_TV_Santa_Fe.png,  5R TV Santa Fe | AR
http://api.new.livestream.com/accounts/22636012/events/8242619/live.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="249" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/249_5TV.png",tvg-id="249" tvg-name="5TV" tvg-logo="https://www.m3u.cl/logo/249_5TV.png,  5TV | AR
http://www.coninfo.net:1935/tvcinco/live1/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="250" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/250_9Link.png",tvg-id="250" tvg-name="9Link" tvg-logo="https://www.m3u.cl/logo/250_9Link.png,  9Link | AR
http://www.coninfo.net:1935/9linklive/live/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="252" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/252_Aire_de_Santa_Fe.png",tvg-id="252" tvg-name="Aire de Santa Fe" tvg-logo="https://www.m3u.cl/logo/252_Aire_de_Santa_Fe.png,  Aire de Santa Fe | AR
https://sc1.stweb.tv/airedigital/live/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="253" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/253_Argentinisima_Satelital.png",tvg-id="253" tvg-name="Argentinisima Satelital" tvg-logo="https://www.m3u.cl/logo/253_Argentinisima_Satelital.png,  Argentinisima Satelital | AR
http://186.0.233.76:1935/Argentinisima/smil:argentinisima.smil/chunklist_sleng.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="215" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/215_Azahares_Radio_Multimedia.png",tvg-id="215" tvg-name="Azahares Radio Multimedia" tvg-logo="https://www.m3u.cl/logo/215_Azahares_Radio_Multimedia.png,  Azahares Radio Multimedia | AR
http://streamyes.alsolnet.com/azaharesfm/live/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="209" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/209_Beat_Digital.png",tvg-id="209" tvg-name="Beat Digital" tvg-logo="https://www.m3u.cl/logo/209_Beat_Digital.png,  Beat Digital | AR
https://5975e06a1f292.streamlock.net:4443/beatvideo/beatvideo/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="224" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/224_Cadena_103.png",tvg-id="224" tvg-name="Cadena 103" tvg-logo="https://www.m3u.cl/logo/224_Cadena_103.png,  Cadena 103 | AR
http://arcast.net:1935/cadena103/cadena103/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="266" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/266_Canal_10.png",tvg-id="266" tvg-name="Canal 10" tvg-logo="https://www.m3u.cl/logo/266_Canal_10.png,  Canal 10 | AR
https://vcp.myplaytv.com:443/canal10cba/smil:canal10cba.smil/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="267" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/267_Canal_10_Mar_del_Plata.png",tvg-id="267" tvg-name="Canal 10 Mar del Plata" tvg-logo="https://www.m3u.cl/logo/267_Canal_10_Mar_del_Plata.png,  Canal 10 Mar del Plata | AR
https://cdn2.zencast.tv:30443/live/canal10smil/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="799" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/799_Canal_10_Nortevision.jpg",tvg-id="799" tvg-name="Canal 10 Nortevision" tvg-logo="https://www.m3u.cl/logo/799_Canal_10_Nortevision.jpg,  Canal 10 Nortevision | AR
https://vivo.solumedia.com:19360/nortevision/nortevision.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="299" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/299_Canal_10_Rio_Negro.png",tvg-id="299" tvg-name="Canal 10 Rio Negro" tvg-logo="https://www.m3u.cl/logo/299_Canal_10_Rio_Negro.png,  Canal 10 Rio Negro | AR
https://panel.dattalive.com:443/8204/8204/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="268" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/268_Canal_12_Madryn_TV.png",tvg-id="268" tvg-name="Canal 12 Madryn TV" tvg-logo="https://www.m3u.cl/logo/268_Canal_12_Madryn_TV.png,  Canal 12 Madryn TV | AR
https://5f700d5b2c46f.streamlock.net:443/madryntv/madryntv/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="226" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/226_Canal_13_Jujuy.png",tvg-id="226" tvg-name="Canal 13 Jujuy" tvg-logo="https://www.m3u.cl/logo/226_Canal_13_Jujuy.png,  Canal 13 Jujuy | AR
https://genexservicios.com:19360/canal13jujuy/canal13jujuy.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="227" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/227_Canal_13_La_Rioja.jpg",tvg-id="227" tvg-name="Canal 13 La Rioja" tvg-logo="https://www.m3u.cl/logo/227_Canal_13_La_Rioja.jpg,  Canal 13 La Rioja | AR
http://arcast.net:1935/mp/mp/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="228" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/228_Canal_2_Jujuy.png",tvg-id="228" tvg-name="Canal 2 Jujuy" tvg-logo="https://www.m3u.cl/logo/228_Canal_2_Jujuy.png,  Canal 2 Jujuy | AR
http://api.new.livestream.com/accounts/679322/events/3782013/live.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="205" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/205_Canal_2_Sanagasta.jpg",tvg-id="205" tvg-name="Canal 2 Sanagasta" tvg-logo="https://www.m3u.cl/logo/205_Canal_2_Sanagasta.jpg,  Canal 2 Sanagasta | AR
https://stmvideo1.livecastv.com/canal2/canal2/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="229" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/229_Canal_20_Villamaria.png",tvg-id="229" tvg-name="Canal 20 Villamaria" tvg-logo="https://www.m3u.cl/logo/229_Canal_20_Villamaria.png,  Canal 20 Villamaria | AR
https://cronos.aldeaglobal.net.ar/hls/canal20.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="1057" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/1057_Canal_21_TV.png",tvg-id="1057" tvg-name="Canal 21 TV" tvg-logo="https://www.m3u.cl/logo/1057_Canal_21_TV.png,  Canal 21 TV | AR
https://iptv.ixfo.com.ar:30443/c21tv/hd/c21tv/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="230" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/230_Canal_22_Buenos_Aires.jpg",tvg-id="230" tvg-name="Canal 22 Buenos Aires" tvg-logo="https://www.m3u.cl/logo/230_Canal_22_Buenos_Aires.jpg,  Canal 22 Buenos Aires | AR
https://5f700d5b2c46f.streamlock.net:443/canal22/canal22/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="271" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/271_Canal_26.png",tvg-id="271" tvg-name="Canal 26" tvg-logo="https://www.m3u.cl/logo/271_Canal_26.png,  Canal 26 | AR
http://live-edge01.telecentro.net.ar/live/smil:c26.smil/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal 26 HD (AR)
https://live-edge01.telecentro.net.ar/live/smil:c26.smil/chunklist.m3u8?ROGERIOTORRES
#EXTINF:-1  tvg-id="776" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/776_Canal_3_La_Pampa.png",tvg-id="776" tvg-name="Canal 3 La Pampa" tvg-logo="https://www.m3u.cl/logo/776_Canal_3_La_Pampa.png,  Canal 3 La Pampa | AR
https://5975e06a1f292.streamlock.net:4443/c3lapampa/ngrp:c3lapampa_all/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="256" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/256_Canal_3_Rosario.png",tvg-id="256" tvg-name="Canal 3 Rosario" tvg-logo="https://www.m3u.cl/logo/256_Canal_3_Rosario.png,  Canal 3 Rosario | AR
https://59d52c5a5ce5e.streamlock.net:4443/canal3rosario/ngrp:canal3rosario_all/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="257" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/257_Canal_4_Bahia_Blanca.png",tvg-id="257" tvg-name="Canal 4 Bahia Blanca" tvg-logo="https://www.m3u.cl/logo/257_Canal_4_Bahia_Blanca.png,  Canal 4 Bahia Blanca | AR
https://vivo.solumedia.com:19360/bvconline/bvconline.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="779" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/779_Canal_4_Eldorado.png",tvg-id="779" tvg-name="Canal 4 Eldorado" tvg-logo="https://www.m3u.cl/logo/779_Canal_4_Eldorado.png,  Canal 4 Eldorado | AR
https://5975e06a1f292.streamlock.net:4443/canal4eldorado/canal4eldorado/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="258" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/258_Canal_4_Jujuy.png",tvg-id="258" tvg-name="Canal 4 Jujuy" tvg-logo="https://www.m3u.cl/logo/258_Canal_4_Jujuy.png,  Canal 4 Jujuy | AR
http://190.52.32.13:1935/canal4/smil:manifest.smil/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="259" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/259_Canal_4_Posadas.png",tvg-id="259" tvg-name="Canal 4 Posadas" tvg-logo="https://www.m3u.cl/logo/259_Canal_4_Posadas.png,  Canal 4 Posadas | AR
http://iptv.ixfo.com.ar:8081/live/C4POS/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="773" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/773_Canal_5_Santa_Fe.png",tvg-id="773" tvg-name="Canal 5 Santa Fe" tvg-logo="https://www.m3u.cl/logo/773_Canal_5_Santa_Fe.png,  Canal 5 Santa Fe | AR
https://5975e06a1f292.streamlock.net:4443/c5sf/c5sf/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="232" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/232_Canal_50_Morteros.png",tvg-id="232" tvg-name="Canal 50 Morteros" tvg-logo="https://www.m3u.cl/logo/232_Canal_50_Morteros.png,  Canal 50 Morteros | AR
http://168.196.255.130:8080/canal50/vivo.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="233" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/233_CANAL_5TV.jpg",tvg-id="233" tvg-name="CANAL 5TV" tvg-logo="https://www.m3u.cl/logo/233_CANAL_5TV.jpg,  CANAL 5TV | AR
https://srv3.zcast.com.br/carlosr/carlosr/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="307" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/307_Canal_6_Entre_Rios.png",tvg-id="307" tvg-name="Canal 6 Entre Rios" tvg-logo="https://www.m3u.cl/logo/307_Canal_6_Entre_Rios.png,  Canal 6 Entre Rios | AR
https://stmvideo1.livecastv.com/canal6er/canal6er/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="261" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/261_Canal_6_Moreno.png",tvg-id="261" tvg-name="Canal 6 Moreno" tvg-logo="https://www.m3u.cl/logo/261_Canal_6_Moreno.png,  Canal 6 Moreno | AR
https://5975e06a1f292.streamlock.net:4443/canal6moreno/canal6moreno/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="262" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/262_Canal_6_Posadas.png",tvg-id="262" tvg-name="Canal 6 Posadas" tvg-logo="https://www.m3u.cl/logo/262_Canal_6_Posadas.png,  Canal 6 Posadas | AR
https://iptv.ixfo.com.ar:30443/live/c6digital/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="264" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/264_Canal_7_Jujuy.png",tvg-id="264" tvg-name="Canal 7 Jujuy" tvg-logo="https://www.m3u.cl/logo/264_Canal_7_Jujuy.png,  Canal 7 Jujuy | AR
https://stream.arcast.live/canal7jujuy/ngrp:canal7jujuy_all/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="234" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/234_Canal_7_Santiago_del_Estero.jpg",tvg-id="234" tvg-name="Canal 7 Santiago del Estero" tvg-logo="https://www.m3u.cl/logo/234_Canal_7_Santiago_del_Estero.jpg,  Canal 7 Santiago del Estero | AR
https://5975e06a1f292.streamlock.net:4443/envivo/castv/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="236" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/236_Canal_9_Litoral.png",tvg-id="236" tvg-name="Canal 9 Litoral" tvg-logo="https://www.m3u.cl/logo/236_Canal_9_Litoral.png,  Canal 9 Litoral | AR
https://stream.arcast.live/ahora/ahora/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="309" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/309_Canal_9_Televida.png",tvg-id="309" tvg-name="Canal 9 Televida" tvg-logo="https://www.m3u.cl/logo/309_Canal_9_Televida.png,  Canal 9 Televida | AR
https://5b3050bb1b2d8.streamlock.net/viviloendirecto2/canal9/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="273" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/273_Canal_907_FM_Comunicar.png",tvg-id="273" tvg-name="Canal 907 FM Comunicar" tvg-logo="https://www.m3u.cl/logo/273_Canal_907_FM_Comunicar.png,  Canal 907 FM Comunicar | AR
https://panel.dattalive.com/canal907/canal907/chunklist_w1205944599.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="274" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/274_Canal_Cinco_Tigre.png",tvg-id="274" tvg-name="Canal Cinco Tigre" tvg-logo="https://www.m3u.cl/logo/274_Canal_Cinco_Tigre.png,  Canal Cinco Tigre | AR
https://59537faa0729a.streamlock.net/cincotv/cincotv/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="275" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/275_Canal_Coop.png",tvg-id="275" tvg-name="Canal Coop" tvg-logo="https://www.m3u.cl/logo/275_Canal_Coop.png,  Canal Coop | AR
https://panel.dattalive.com:443/8138/8138/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="302" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/302_Canal_Nueve_TV.png",tvg-id="302" tvg-name="Canal Nueve TV" tvg-logo="https://www.m3u.cl/logo/302_Canal_Nueve_TV.png,  Canal Nueve TV | AR
https://live.canalnueve.tv/canal.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="801" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/801_Canal_Provincial.jpg",tvg-id="801" tvg-name="Canal Provincial" tvg-logo="https://www.m3u.cl/logo/801_Canal_Provincial.jpg,  Canal Provincial | AR
https://streaming.telered.com.ar/provincial/streaming/mystream.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="203" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/203_Catamarca_TV.png",tvg-id="203" tvg-name="Catamarca TV" tvg-logo="https://www.m3u.cl/logo/203_Catamarca_TV.png,  Catamarca TV | AR
https://5f700d5b2c46f.streamlock.net/catamarcatelevision/catamarcatelevision/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="278" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/278_Chacra_TV.png",tvg-id="278" tvg-name="Chacra TV" tvg-logo="https://www.m3u.cl/logo/278_Chacra_TV.png,  Chacra TV | AR
https://s8.stweb.tv/chacra/live/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="237" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/237_Ciudad_TV.jpg",tvg-id="237" tvg-name="Ciudad TV" tvg-logo="https://www.m3u.cl/logo/237_Ciudad_TV.jpg,  Ciudad TV | AR
http://coninfo.net:1935/chacodxdtv/live/chunklist_w1251301598.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="280" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/280_CL3_Cablevision.png",tvg-id="280" tvg-name="CL3 Cablevision" tvg-logo="https://www.m3u.cl/logo/280_CL3_Cablevision.png,  CL3 Cablevision | AR
http://videostream.shockmedia.com.ar:1935/cl3cable/cl3cable/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="270" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/270_CN_24_7_Neuquen.png",tvg-id="270" tvg-name="CN 24/7 Neuquen" tvg-logo="https://www.m3u.cl/logo/270_CN_24_7_Neuquen.png,  CN 24/7 Neuquen | AR
https://panel.dattalive.com:443/6605140/smil:6605140.smil/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="893" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/893_Complejo_Dance.png",tvg-id="893" tvg-name="Complejo Dance" tvg-logo="https://www.m3u.cl/logo/893_Complejo_Dance.png,  Complejo Dance | AR
https://mediacp.hostradios.com.ar:19360/complejodance/complejodance.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="238" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/238_CPE_TV.jpg",tvg-id="238" tvg-name="CPE TV" tvg-logo="https://www.m3u.cl/logo/238_CPE_TV.jpg,  CPE TV | AR
https://stream.arcast.live/cpe/ngrp:cpe_all/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="239" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/239_Fenix.jpg",tvg-id="239" tvg-name="Fenix" tvg-logo="https://www.m3u.cl/logo/239_Fenix.jpg,  Fenix | AR
https://stmvideo1.livecastv.com/fenixlarioja/fenixlarioja/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="803" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/803_FM_Metropolitana_100_5_MHZ.png",tvg-id="803" tvg-name="FM Metropolitana 100.5 MHZ" tvg-logo="https://www.m3u.cl/logo/803_FM_Metropolitana_100_5_MHZ.png,  FM Metropolitana 100.5 MHZ | AR
https://streamtv12.ddns.net:5443/LiveApp/streams/193945633734205616732920.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="216" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/216_Informacion_Periodistica.jpg",tvg-id="216" tvg-name="Informacion Periodistica" tvg-logo="https://www.m3u.cl/logo/216_Informacion_Periodistica.jpg,  Informacion Periodistica | AR
https://d1nmqgphjn0y4.cloudfront.net/live/ip/live.isml/5ee6e167-1167-4a85-9d8d-e08a3f55cff3.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="217" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/217_La_Voz_de_Tucuman.png",tvg-id="217" tvg-name="La Voz de Tucuman" tvg-logo="https://www.m3u.cl/logo/217_La_Voz_de_Tucuman.png,  La Voz de Tucuman | AR
https://srv1.zcast.com.br/lavozdetucuman/lavozdetucuman/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="212" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/212_Link_TV.png",tvg-id="212" tvg-name="Link TV" tvg-logo="https://www.m3u.cl/logo/212_Link_TV.png,  Link TV | AR
https://panel.dattalive.com:443/8128_1/8128_1/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="241" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/241_Litus_TV.png",tvg-id="241" tvg-name="Litus TV" tvg-logo="https://www.m3u.cl/logo/241_Litus_TV.png,  Litus TV | AR
https://5975e06a1f292.streamlock.net:4443/litustv/ngrp:litustv_all/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="283" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/283_Metro_TV_Canal_12_Tucuman.png",tvg-id="283" tvg-name="Metro TV Canal 12 Tucuman" tvg-logo="https://www.m3u.cl/logo/283_Metro_TV_Canal_12_Tucuman.png,  Metro TV Canal 12 Tucuman | AR
https://streamtv12.ddns.net:5443/LiveApp/streams/193945633734205616732920.m3u8?token=null&PlaylistM3UCL
#EXTINF:-1  tvg-id="795" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/795_Metropolitana_FM.png",tvg-id="795" tvg-name="Metropolitana FM" tvg-logo="https://www.m3u.cl/logo/795_Metropolitana_FM.png,  Metropolitana FM | AR
https://panel.dattalive.com/MetropolitanaFM/MetropolitanaFM/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="793" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/793_Milenium_TV.png",tvg-id="793" tvg-name="Milenium TV" tvg-logo="https://www.m3u.cl/logo/793_Milenium_TV.png,  Milenium TV | AR
https://tuvideoonline.com.ar:3994/live/mileniumtvlive.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="284" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/284_Multivision.png",tvg-id="284" tvg-name="Multivisi n" tvg-logo="https://www.m3u.cl/logo/284_Multivision.png,  Multivisi n | AR
https://panel.dattalive.com:443/8250/8250/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="285" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/285_Net_TV.png",tvg-id="285" tvg-name="Net TV" tvg-logo="https://www.m3u.cl/logo/285_Net_TV.png,  Net TV | AR
https://unlimited1-cl-isp.dps.live/nettv/nettv.smil/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="243" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/243_Power.png",tvg-id="243" tvg-name="Power" tvg-logo="https://www.m3u.cl/logo/243_Power.png,  Power | AR
https://live2.tensila.com/1-1-1.power-tv/hls/master.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="912" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/912_Radio_Blu.png",tvg-id="912" tvg-name="Radio Blu" tvg-logo="https://www.m3u.cl/logo/912_Radio_Blu.png,  Radio Blu | AR
https://59537faa0729a.streamlock.net:443/radioblu/radioblu/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="210" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/210_Radiocanal_San_Francisco.png",tvg-id="210" tvg-name="Radiocanal San Francisco" tvg-logo="https://www.m3u.cl/logo/210_Radiocanal_San_Francisco.png,  Radiocanal San Francisco | AR
http://204.199.3.2/.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="287" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/287_RTN.png",tvg-id="287" tvg-name="RTN" tvg-logo="https://www.m3u.cl/logo/287_RTN.png,  RTN | AR
http://media.neuquen.gov.ar/rtn/television/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="202" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/202_San_Pedro_TV.png",tvg-id="202" tvg-name="San Pedro TV" tvg-logo="https://www.m3u.cl/logo/202_San_Pedro_TV.png,  San Pedro TV | AR
https://srv6.zcast.com.br/sptv/sptv/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="288" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/288_Sicardi_TV.png",tvg-id="288" tvg-name="Sicardi TV" tvg-logo="https://www.m3u.cl/logo/288_Sicardi_TV.png,  Sicardi TV | AR
https://vivo.solumedia.com:19360/sicarditv/sicarditv.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="1072" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/1072_Somos_La_Pampa.png",tvg-id="1072" tvg-name="Somos La Pampa" tvg-logo="https://www.m3u.cl/logo/1072_Somos_La_Pampa.png,  Somos La Pampa | AR
https://5975e06a1f292.streamlock.net:4443/somosnoticias/somosnoticias/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="289" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/289_TDC_TV_Santa_Fe.png",tvg-id="289" tvg-name="TDC TV Santa Fe" tvg-logo="https://www.m3u.cl/logo/289_TDC_TV_Santa_Fe.png,  TDC TV Santa Fe | AR
https://5e7cdf2370883.streamlock.net/tdconline/tdconline/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="308" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/308_Tele_Estrella.png",tvg-id="308" tvg-name="Tele Estrella" tvg-logo="https://www.m3u.cl/logo/308_Tele_Estrella.png,  Tele Estrella | AR
https://stmvideo2.livecastv.com/telestrella/telestrella/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="290" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/290_Telecreativa.png",tvg-id="290" tvg-name="Telecreativa" tvg-logo="https://www.m3u.cl/logo/290_Telecreativa.png,  Telecreativa | AR
https://panel.dattalive.com:443/8012/8012/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="291" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/291_Telediario_Television.png",tvg-id="291" tvg-name="Telediario Televisi n" tvg-logo="https://www.m3u.cl/logo/291_Telediario_Television.png,  Telediario Televisi n | AR
https://mediacp.hostradios.com.ar:19360/telediario/telediario.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="245" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/245_Telediez.jpg",tvg-id="245" tvg-name="Telediez" tvg-logo="https://www.m3u.cl/logo/245_Telediez.jpg,  Telediez | AR
https://videohd.live:19360/8020/8020.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="246" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/246_Telefe_Rosario.jpg",tvg-id="246" tvg-name="Telefe Rosario" tvg-logo="https://www.m3u.cl/logo/246_Telefe_Rosario.jpg,  Telefe Rosario | AR
http://telefewhitehls-lh.akamaihd.net/i/whitelist_hls@302302/master.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="292" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/292_Telemax.png",tvg-id="292" tvg-name="Telemax" tvg-logo="https://www.m3u.cl/logo/292_Telemax.png,  Telemax | AR
http://live-edge01.telecentro.net.ar/live/smil:tlx.smil/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="814" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/814_TeleNord.jpg",tvg-id="814" tvg-name="TeleNord" tvg-logo="https://www.m3u.cl/logo/814_TeleNord.jpg,  TeleNord | AR
http://www.coninfo.net:1935/previsoratv/live/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="295" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/295_Telesol_San_Juan.png",tvg-id="295" tvg-name="Telesol San Juan" tvg-logo="https://www.m3u.cl/logo/295_Telesol_San_Juan.png,  Telesol San Juan | AR
https://cnnsanjuan.com:9999/live/telesol/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="293" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/293_Telpin_Canal_2.png",tvg-id="293" tvg-name="Telpin Canal 2" tvg-logo="https://www.m3u.cl/logo/293_Telpin_Canal_2.png,  Telpin Canal 2 | AR
https://wowza.telpin.com.ar:1935/telpintv/smil:ttv.stream.smil/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="294" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/294_Terramia_TV.png",tvg-id="294" tvg-name="Terramia TV" tvg-logo="https://www.m3u.cl/logo/294_Terramia_TV.png,  Terramia TV | AR
https://live-edge01.telecentro.net.ar/live/smil:trm.smil/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="777" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/777_Tribu_TV.jpg",tvg-id="777" tvg-name="Tribu TV" tvg-logo="https://www.m3u.cl/logo/777_Tribu_TV.jpg,  Tribu TV | AR
https://5975e06a1f292.streamlock.net:4443/tributv/tributv/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="296" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/296_TSN_Necochea.png",tvg-id="296" tvg-name="TSN Necochea" tvg-logo="https://www.m3u.cl/logo/296_TSN_Necochea.png,  TSN Necochea | AR
https://panel.dattalive.com:443/tsnnecochea/tsnnecochea/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="788" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/788_TV_Dos_Salta.jpg",tvg-id="788" tvg-name="TV Dos Salta" tvg-logo="https://www.m3u.cl/logo/788_TV_Dos_Salta.jpg,  TV Dos Salta | AR
https://vivo.solumedia.com:19360/tv2salta/tv2salta.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="297" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/297_TV_Mana.png",tvg-id="297" tvg-name="TV Mana" tvg-logo="https://www.m3u.cl/logo/297_TV_Mana.png,  TV Mana | AR
http://csvl03.manasat.com:1935/tvar/tvmanaar2/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="248" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/248_Uni_Teve.png",tvg-id="248" tvg-name="Uni Teve" tvg-logo="https://www.m3u.cl/logo/248_Uni_Teve.png,  Uni Teve | AR
https://vivo.solumedia.com:19360/uniteve/uniteve.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="304" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/304_UTN_TV.png",tvg-id="304" tvg-name="UTN TV" tvg-logo="https://www.m3u.cl/logo/304_UTN_TV.png,  UTN TV | AR
https://5975e06a1f292.streamlock.net:4443/utntv/utntv/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="1100" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/1100_DEPORTV.png",tvg-id="1100" tvg-name="DEPORTV" tvg-logo="https://www.m3u.cl/logo/1100_DEPORTV.png,  DEPORTV | AR
https://5fb24b460df87.streamlock.net/live-cont.ar/deportv/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="282" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/282_Garage_TV.png",tvg-id="282" tvg-name="Garage TV" tvg-logo="https://www.m3u.cl/logo/282_Garage_TV.png,  Garage TV | AR
http://186.0.233.76:1935/Garage/smil:garage.smil/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="493" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/493_Net_TV.png",tvg-id="493" tvg-name="Net TV" tvg-logo="https://www.m3u.cl/logo/493_Net_TV.png,  Net TV | AR
https://unlimited1-cl-isp.dps.live/nettv/nettv.smil/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="492" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/492_TV_Publica.png",tvg-id="492" tvg-name="TV Publica" tvg-logo="https://www.m3u.cl/logo/492_TV_Publica.png,  TV Publica | AR
https://g1.vxral-hor.transport.edge-access.net/b16/ngrp:c7_vivo01_dai_source-20001_all/c7_vivo01_dai_source-20001.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="24" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/24_Music_Top.png",tvg-id="24" tvg-name="Music Top" tvg-logo="https://www.m3u.cl/logo/24_Music_Top.png,  Music Top | AR
http://live-edge01.telecentro.net.ar/live/smil:musictop.smil/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="208" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/208_CINE_AR.png",tvg-id="208" tvg-name="CINE.AR" tvg-logo="https://www.m3u.cl/logo/208_CINE_AR.png,  CINE.AR | AR
https://5fb24b460df87.streamlock.net/live-cont.ar/cinear/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="207" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/207_Orbe_21.jpg",tvg-id="207" tvg-name="Orbe 21" tvg-logo="https://www.m3u.cl/logo/207_Orbe_21.jpg,  Orbe 21 | AR
https://cdn2.zencast.tv:30443/orbe/orbe21smil/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="1003" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/1003_Sublime_Gracia_TV.png",tvg-id="1003" tvg-name="Sublime Gracia TV" tvg-logo="https://www.m3u.cl/logo/1003_Sublime_Gracia_TV.png,  Sublime Gracia TV | AR
https://5f700d5b2c46f.streamlock.net:443/sublime/sublime/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",El nueve
https://rbmn-live.akamaized.net/hls/live/590971/201212BatallaWorldFinalPri/master.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",El nueve
https://00475e6934d74fe48a80427567a45918.mediatailor.us-east-1.amazonaws.com/v1/master/4c8323052bc3dbd9aa2eba0b638d8495561e8377/JW-Octubre-Channel09/live/channel09/live.isml/b00d164f-be51-473e-a47c-b33aa1f44186.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="https://www.cxtv.com.br/img/Tvs/Logo/webp-l/d800ee1a28bbee6769de24c5c050c40c.webp",Canal Once
https://vivo.canaloncelive.tv/alivepkgr3/ngrp:cepro_all/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Aire de Santa Fe TV
https://sc1.stweb.tv/airedigital/live/chunklist_w1407250980.m3u8

#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",DEPORTV
https://5fb24b460df87.streamlock.net/live-cont.ar/deportv/chunklist.m3u8


#EXTINF:-1, FoxSports 
https://edge01-fdo-py.cvattv.com.ar/live/c3eds/FoxSports/SA_SAGEMCOM/FoxSports.m3u8

#EXTINF:-1, FoxSports 2 
https://edge01-fdo-py.cvattv.com.ar/live/c3eds/FoxSports2HD/SA_SAGEMCOM/FoxSports2HD.m3u8

#EXTINF:-1, FoxSports 3 
https://edge01-fdo-py.cvattv.com.ar/live/c3eds/FoxSports3HD/SA_SAGEMCOM/FoxSports3HD.m3u8

#EXTINF:-1, ESPN2 
https://edge01-fdo-py.cvattv.com.ar/live/c3eds/ESPN2HD/SA_SAGEMCOM/ESPN2HD.m3u8

#EXTINF:-1, ESPN4 
https://edge01-fdo-py.cvattv.com.ar/live/c7eds/ESPN4/SA_SAGEMCOM/ESPN4.m3u8

#EXTINF:-1, DeporTV 
https://edge01-fdo-py.cvattv.com.ar/live/c3eds/DeporTVHD/SA_SAGEMCOM/DeporTVHD.m3u8

#EXTINF:-1, TYC SPORT

https://d3awnlgqz0szay.cloudfront.net/out/v1/b841c366cbe540e6a106c3ba83e5c8d6/index.m3u8

#EXTINF:-1, FOX SPORT PREMIUM 
https://edge10-hr.cvattv.com.ar/live/c3eds/Fox_Sports_Premiun_HD/SA_SAGEMCOM/Fox_Sports_Premiun_HD-avc1_4999936=10000.m3u8

#EXTINF:-1, TNT SPORT 
https://edge7-ccast-hr.cvattv.com.ar/live/c3eds/TNT_Sports_HD/SA_SAGEMCOM/TNT_Sports_HD-avc1_899968=10009.m3u8

#EXTINF:-1 tvg-logo="http://rockypoint360.com/rocky-point-business-directory/wp-content/uploads/2015/10/logo-megacable_1.jpg", CINEMAX 
https://edge2-ccast-sl.cvattv.com.ar/live/c6eds/Cinemax/SA_SAGEMCOM/Cinemax.m3u8

#EXTINF:-1, HBO 
https://edge2-ccast-sl.cvattv.com.ar/live/c3eds/HBOHD/SA_SAGEMCOM/HBOHD.m3u8

#EXTINF:-1, HBO 2 
https://edge2-ccast-sl.cvattv.com.ar/live/c6eds/HBO_2/SA_SAGEMCOM/HBO_2.m3u8

#EXTINF:-1, HBO PLUS 
https://edge2-ccast-sl.cvattv.com.ar/live/c6eds/HBO_Plus/SA_SAGEMCOM/HBO_Plus.m3u8

#EXTINF:-1, HBO FAMILY 
https://edge2-ccast-sl.cvattv.com.ar/live/c6eds/HBO_Family/SA_SAGEMCOM/HBO_Family.m3u8

#EXTINF:-1, HBO POP 
https://edge2-ccast-sl.cvattv.com.ar/live/c7eds/HBO_POP/SA_SAGEMCOM/HBO_POP.m3u8

#EXTINF:-1, HBO MUNDI 
https://edge2-ccast-sl.cvattv.com.ar/live/c6eds/HBO_Mundi/SA_SAGEMCOM/HBO_Mundi.m3u8

#EXTINF:-1, HBO EXTREME 
https://edge2-ccast-sl.cvattv.com.ar/live/c6eds/HBO_Extreme/SA_SAGEMCOM/HBO_Extreme.m3u8

#EXTINF:-1, FOX HD 
https://edge2-ccast-sl.cvattv.com.ar/live/c3eds/FOXHD/SA_SAGEMCOM/FOXHD.m3u8

#EXTINF:-1, 
DiscoveryHomeHealth https://edge01-fdo-py.cvattv.com.ar/live/c3eds/DiscoveryHomeHealthHD/SA_SAGEMCOM/DiscoveryHomeHealthHD.m3u8

#EXTINF:-1, Warner 
https://edge01-fdo-py.cvattv.com.ar/live/c7eds/WarnerHD/SA_SAGEMCOM/WarnerHD.m3u8

#EXTINF:-1, Sony
 https://edge01-fdo-py.cvattv.com.ar/live/c7eds/SonyHD/SA_SAGEMCOM/SonyHD.m3u8

#EXTINF:-1, AXN
 https://edge01-fdo-py.cvattv.com.ar/live/c7eds/AXNHD/SA_SAGEMCOM/AXNHD.m3u8

#EXTINF:-1, Cinecanal 
https://edge01-fdo-py.cvattv.com.ar/live/c3eds/CinecanalHD/SA_SAGEMCOM/CinecanalHD.m3u8

#EXTINF:-1, Paramount 
https://edge01-fdo-py.cvattv.com.ar/live/c7eds/Paramount/SA_SAGEMCOM/Paramount.m3u8

#EXTINF:-1, Space 
https://latam2-lh.akamaihd.net/i/SPA_SUR@445604/master.m3u8?hdnea=st=1647214285~exp=1647214885~acl=/*~hmac=cec3028403d02ddc00850524568731ac5c1a4af3bba8cb28f1417613fa24dbf2

#EXTINF:-1, TNT 
https://edge01-fdo-py.cvattv.com.ar/live/c3eds/TNT_HD_Arg/SA_SAGEMCOM/TNT_HD_Arg.m3u8

#EXTINF:-1, TNTSeries 
https://edge01-fdo-py.cvattv.com.ar/live/c3eds/TNTSeries/SA_SAGEMCOM/TNTSeries.m3u8

#EXTINF:-1, Universal_Channel 
https://edge01-fdo-py.cvattv.com.ar/live/c6eds/Universal_Channel_HD/SA_SAGEMCOM/Universal_Channel_HD.m3u8

#EXTINF:-1, BabyTV 
https://edge01-fdo-py.cvattv.com.ar/live/c7eds/BabyTV/SA_SAGEMCOM/BabyTV-avc1_1532000=10004.m3u8

#EXTINF:-1, Tooncast
 https://edge01-fdo-py.cvattv.com.ar/live/c6eds/Tooncast/SA_SAGEMCOM/Tooncast.m3u8


#EXTINF:-1 tvg-chno-"63",LA VOZ DE TUCUMAN
https://srv1.zcast.com.br/lavozdetucuman/lavozdetucuman/.m3u8

#EXTINF:-1 tvg-chno-"63",UNIVERSITARIA MAR DEL PLATA
https://stream-02.nyc.dailymotion.com/sec(SCEOt4M5U0fVbrIPRLL54yT7QpB8ZtsTHlr597Z4UHU)/dm/3/x7kvvgi/s/live-1.m3u8


'''

import requests
import os
import sys

windows = False
if 'win' in sys.platform:
    windows = True

def grab(url):
    response = requests.get(url, timeout=15).text
    if '.m3u8' not in response:
        #response = requests.get(url).text
        if '.m3u8' not in response:
            if windows:
                print('https://raw.githubusercontent.com/guiworldtv/MEU-IPTV-FULL/main/VideoOFFAir.m3u8')
                return
            os.system(f'wget {url} -O temp.txt')
            response = ''.join(open('temp.txt').readlines())
            if '.m3u8' not in response:
                print('https://raw.githubusercontent.com/guiworldtv/MEU-IPTV-FULL/main/VideoOFFAir.m3u8')
                return
    end = response.find('.m3u8') + 5
    tuner = 100
    while True:
        if 'https://' in response[end-tuner : end]:
            link = response[end-tuner : end]
            start = link.find('https://')
            end = link.find('.m3u8') + 5
            break
        else:
            tuner += 5
    print(f"{link[start : end]}")

print('#EXTM3U x-tvg-url="https://iptv-org.github.io/epg/guides/ar/mi.tv.epg.xml"')
print('#EXTM3U x-tvg-url="https://raw.githubusercontent.com/mudstein/XML/main/TIZENsiptv.xml"')
print('#EXTM3U x-tvg-url="https://raw.githubusercontent.com/K-vanc/Tempest-EPG-Generator/main/Siteconfigs/Argentina/%5BENC%5D%5BEX%5Delcuatro.com_0.channel.xml"')
print('#EXTM3U x-tvg-url="https://raw.githubusercontent.com/Nicolas0919/Guia-EPG/master/GuiaEPG.xml"')

#s = requests.Session()
with open('../ARGENTINA.txt', errors="ignore") as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith('~~'):
            continue
        if not line.startswith('https:'):
            line = line.split('|')
            ch_name = line[0].strip()
            grp_title = line[1].strip().title()
            tvg_logo = line[2].strip()
            tvg_id = line[3].strip()
            print(f'\n#EXTINF:-1 group-title="{grp_title}" tvg-logo="{tvg_logo}" tvg-id="{tvg_id}", {ch_name}')
        else:
            grab(line)
print(banner)            
if 'temp.txt' in os.listdir():
    os.system('rm temp.txt')
    os.system('rm watch*')
    
    


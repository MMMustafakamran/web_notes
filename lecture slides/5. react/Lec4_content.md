# Content from Lec4.pdf

## Page 1

LECTURE #4
By: Aqib Rehman

J J J V LECTURE #4 By: Aqib Rehman

*(Extracted via OCR)*


---

## Page 2

OUTLINE
Conditional Output
Forms Revisited
Functions as Props


---

## Page 3

CONDITIONAL OUTPUT

CONDITIONAL OUTPUT

*(Extracted via OCR)*


---

## Page 4

Nap Nilasjs Limport React from react 0 const Ninjas ({ninjas}) 8 const ninjalist ninjas map(ninja 3> 5 if (ninja age 20) { 6 return <div className-"ninja" key-{ninja id D (div>Nane: ninja name } </div> div Age: ninja age } </div> 10 Idiv>Belt: ninja belt }/div 11 Idiv> 12 13 else 14 return null 15 16 17 return( 18 <div className-"ninja-list"> 19 ninjalist 0 Kldiv 724 2

*(Extracted via OCR)*


### Images:

![page_4_img_1.jpeg](Lec4_images/page_4_img_1.jpeg)


---

## Page 5

4ke Buneo Elements Sources Console Network My first React appl Filter Default levels Group similar 0 8 Welcome :) Name: Ryu Age: 30 Belt: black Name: Crystal Age: 25 Belt: pink top

*(Extracted via OCR)*


### Images:

![page_5_img_1.png](Lec4_images/page_5_img_1.png)


---

## Page 6

Np Ntasj 'import React from react 90 const Ninjas ({ninjas}) % 1 const ninjalist ninjas map(ninja 37 [ 5 if (ninja age 20) { 0 return div classNames"ninja key {ninja id}> D sdiv Name: ninja name }</div> <div Age: ninja age }</div? div Belt: (ninja belt } /div? % 1 Rispaiv F14 return null 15 16 17 const ninjalist ninjas map(ninja 18 kondition 419 20 return( l Xdiv €lassNane "ninja-list" 1, ninjalist

*(Extracted via OCR)*


### Images:

![page_6_img_1.jpeg](Lec4_images/page_6_img_1.jpeg)


---

## Page 7

No Import React from react 0 const Ninjas ({ninjas}) 8 4 const ninjalist ninjas.map(ninja 3d { 5 if (ninja.age 20) { Feturn div classNames"ninja key-{ninja.id} > 4 div Name : (ninja.name }/div> xdiv Age: {ninja age }< /div) 10 (div Belt: {ninja.belt k/div> kldivs % 1 } else { return null 15 16 17 const ninjalist ninjas map(ninja 3> 18 return ninja age 20 pull 19 70 return( 1 <div classMames"ninja-list" Cy ninjalist

*(Extracted via OCR)*


### Images:

![page_7_img_1.jpeg](Lec4_images/page_7_img_1.jpeg)


---

## Page 8

Npp Nujs Import Keact Frcr react 0 3 const Ninjas ({ninjas}) const ninjalist ninjas map(ninja Eol { 5 if (ninja.age 20) { 6 return Xdiv className-"ninja" key-{ninja.id}> div Name {ninja,name } /div> <div Age: [Eninja.age }</div> 10 Kdiv Belt: ninja belt }/div> Kldiv> 12 13 }else [ 14 return null 15 016 17 const ninjalist ninjas map(ninja  18 return ninja age 20 19 <div className "ninja key-{ninja id 20 div>Name: ninja name } </div> 71 <div Age: ninja age }</div= 22 <divsBelt: ninja belt }<ldiv> 23 'div> 24 null; 25 H; 26 return

*(Extracted via OCR)*


### Images:

![page_8_img_1.jpeg](Lec4_images/page_8_img_1.jpeg)


---

## Page 9

TFais =ed 0 Abojs Nuyarjs 845e 14 return null 0 15 8 1o 17 const ninjalist ninjas map(ninja 18 return ninja age 20 19 <div  className:"ninja" {ninja id D 20 div>Name ninja name } </div> 21 div Age: ninja age } </div> 22 div Belt: ninja belt }</div> 2J Idiv> 24 null; 75 726 27 return 28 <div const ninjalist any 70 ninjalist 0 kldiv 01 32 33 E4 export default Ninjas keya

*(Extracted via OCR)*


### Images:

![page_9_img_1.jpeg](Lec4_images/page_9_img_1.jpeg)


---

## Page 10

Nap Nj 8436 1d return null 0 15 8 16 17 0 18 419 return G 20 Kdiv classNane= "ninja-list"> 21 ninjaList 2 div> 23 4 25 26 export default Ninjas

*(Extracted via OCR)*


### Images:

![page_10_img_1.jpeg](Lec4_images/page_10_img_1.jpeg)


---

## Page 11

4 Notnjs 18486 14 return null 0 15 8 16 17 18 10 ceturn( 70 <div €lassName "ninja-list" 21 22 ninjas map(ninja 23 return ninja age 20 a div className "ninja" key-{ninja id 25 divsName: ninja name }</div> 26 div Age: ninja age } </div> 27 div>Belt: ninja belt }</div> 8 diva 29 null; 30 31 32 kldiv> 33 Ja  35 36 export default Ninjas

*(Extracted via OCR)*


### Images:

![page_11_img_1.jpeg](Lec4_images/page_11_img_1.jpeg)


---

## Page 12

FORMS REVISITED

FORMS REVISITED

*(Extracted via OCR)*


---

## Page 13

What we have already

0 0 My first React appl Welcome :) Name: Ryu Age: 30 Belt; black Name: Crystal Age; 25 Belt: pink What we have already

*(Extracted via OCR)*


### Images:

![page_13_img_1.jpeg](Lec4_images/page_13_img_1.jpeg)


---

## Page 14

WHAT WE GONNA DO
A form in which user can add new ninja of his/her choice.
Programmatically how?
What if by some method we update the ninjas list which we have defined in state of 
App comp.
This list passes as props to Ninjas comp, where it is iterate and show on the screen.
So when list will be updated the updated one will be sent to Ninjas component and 
that will be shown to the user.
So lets create a form with 3 fields for name, age, belt and add button.


---

## Page 15

Create a new component with name AddNinja

Create a new component with name AddNinja

*(Extracted via OCR)*


---

## Page 16

EACT Man AoNinkap ortmtoton 0 San Hatelvg A Ninbr U JEACT EEDUX CDVPLEE Epp Moc_ncdule Duble Rakenito Hmennitmi ManeSLjecn Addrenaj ppn Hmiaan Jndcan Ninkatn KenistetScrvicewonerK oience Badag  odyn Dacekon eADHenid

*(Extracted via OCR)*


### Images:

![page_16_img_1.jpeg](Lec4_images/page_16_img_1.jpeg)


---

## Page 17

What will be type of this comp container or stateless?


---

## Page 18

As we want to store user input values locally in the state so container comp will be 
used


---

## Page 19

htmlFor in jsx template not for

BACSE Aban AXNinp Ortntonons Icpont React , (~Component } from react Mok Aniue 2 Aaaninan 3 class AddNinja extends Component { REACI RIDUX COMNEE Mapp render() { noor_odulc 5 ceturn publc 0 div Hartorto 7/ formy Hinatatmi anielyjsen 8 label htalfor_ name" > Name:< /labele 9 Input type "text: ds nane onchange-{ } ddranlaj 10 label htnlfora 'nane">Age:</label Apor T1 input cypea"text ide age onchange-(} Inore 17 label htnlfora name"> Belti /label Jnetk Ninan 15 Input LypC= text Ide"belt onchanger (] icglste Scrwcconerh 14 buttonsSubmit-/button oienoe 15 forn ~pedea Hlodkjion 16 kldiva packiaRon REDMEd 17 18 19 htmlFor in jsx template not for

*(Extracted via OCR)*


### Images:

![page_19_img_1.jpeg](Lec4_images/page_19_img_1.jpeg)


---

## Page 20

Define state

ETCein Han ANlinay Ortmtoroi Inport React , Component Afrom react 0 Mof 2n 4a' Ninaa Wndet class AddNinja extends Component REACT FIDUK CONPLEIE 8 Ep state nobe_ncdule name null publ agC null Tatkerco belt: null Anatknl mnanttaton render () { Adurenaj 8 return npr 11 di> Uet 12 form Anana Ninitn 13 label htmlfor_"name">Name: khlabel Acgiste scrvcetolian 1 input type "text id= nane onchangez{} Oinate 15 label htalfor_"nane",Age:</label padktg  lockjen 16 input type-"text" id = age 'onchange=[} DadieHon PEDhnd 17 label htalFore 'nane"> Belt:s label> 18 input type"text" id-"belt" onchanger{ 19 button Submita/button 78 Farm Al div> S Define state

*(Extracted via OCR)*


### Images:

![page_20_img_1.jpeg](Lec4_images/page_20_img_1.jpeg)


---

## Page 21

Need 3 functions for each field. 
Right?
No

Need 3 functions for each field: Right? No

*(Extracted via OCR)*


---

## Page 22

BPLCAER MAnan ANinjap OPLNIDnORS IiLo Limport React , {Component from react 0 Mar @nnolug Adonina s  tyandaE class AddNinja extends Component { auac RIDuK conplll mapp state node Medules name null publkc age null Tarkonco belt : null iaantml manllestjsc a handleChange AddNinja js o this setState( { Appj 11 [e.target.id] target value Incros 12 Indcrk Ninjask 13 tcgistc Scnncc Voncj 14 render() { gllgnore 15 Feturo package-lockjson 16 adiv> padagekon READHNE nid 17 (formy 18 label htmlFor_"name">Name: < /label- 419 input typea"text ide"name onchange-[ 20 label htmlFor "name" Age: </label 21 input type"text id-"age onchange {} 7> Beld

*(Extracted via OCR)*


### Images:

![page_22_img_1.jpeg](Lec4_images/page_22_img_1.jpeg)


---

## Page 23

Calling handleChange func

BACATR N AONinjap opcnEdMORS Fnne import React , Component From 'react 0 Mof atplvr odNinats myappidc HDUX COKPLEI class AddNinja extends Component { FEaCT Mapp state nocemedule name null, pubor age: null Tatkouco belt : null Inderninil manllestjson handleChange (e) AddNinjajs 0 this setState( { ppjs l [e.target id] e . target value Hnderess 12 nderk Ninjasj 3 icqistersericcWVorecrjs J4 render() { glugnare 15 return package-lockjion 16 div packagetson READMEmd 17 forn 8 label htmlfor_ name"> Name Klabel 19 Input type "text Id= name onchange-{this handleChange} 10 label htmlfor= 'name" >Age: < /label> 1 input type "text id-"age' onChange-{this handleChange 1> 722 labe] htm]For = 'name">Belt:</label 23 input type "text: id "belt onchange-Ithis handleChangel a <button Submitk/button> 25 form Calling handleChange func

*(Extracted via OCR)*


### Images:

![page_23_img_1.jpeg](Lec4_images/page_23_img_1.jpeg)


---

## Page 24

hanldeSubmit func

EACEER App j AnNlirap OPENEDuORS Uaato 06~ Apar myertiut belt null AdoNina  Inyonolyc BEACT-RIOUX colpleuE handleChange (e) 8 Myapp 0 this setStatel { noce nadulc, ~publk l [e.target.id] e target-value Jatcaico 12 H) naer neml J ~manitestjscn 4 handleSubmit (e) EC 05 preventDefault(); AddNInjajs App js o console log(this state) ; Indoross 17 Incj 018 render() { Ninjasp 49 return Tgiste ScrviccMorcr js 20 div gibgnore ~package-lockjion 71 formi onSubmit-[this handleSubmit ~packagesson 22 label htmlfor= name" > Name : < /label README md 73 <input type text id name onchange-{this handleChange 1> 24 label htmifor= name"> Age:< /label 75 input type= text de age onChange= this handleChange 7 > 26 (label htrlfor name"> Belti/label 37 Input type "text id 'belt" onchange-{this handleChange 1 > 78 <button Submite/button hanldeSubmit func

*(Extracted via OCR)*


### Images:

![page_24_img_1.jpeg](Lec4_images/page_24_img_1.jpeg)


---

## Page 25

Adding AddNinja comp in the root comp

EXFCFTR App js AoNinan OpcntDuors Uvadtd import React , {Component } from react Appk myenetrt import Ninjas from INinjas AddNinan mynpplue import AddNinja fron /AddNinja Reaci-rldux-Complnt mapp noor_micdules class App extends Component pubkc state Tukonico 7 ninjas Jnerntml mnanllestjsen name Ryu' age : 30, belt: black id: 1 }, name  Yoshi age : 20, belt green id; AddNinjajs 10 name Crystal' age : 25 belt: 'pink' id: 3 } App p 1 Hrderos 12 inerp Ninjatf 13 render() registcrScrviccioricr Js 64 Feturn plugnorc 15 <div classNane "App" package lock jion 116 <hlxly first React appl</hl> padagepon README Id 17 >Nelcone 9< 18 <Ninjas ninjase{this state ninjas} 19 RAddNinja 20 div> 3 ; 7 F6 Adding AddNinja comp in the root comp 2 %

*(Extracted via OCR)*


### Images:

![page_25_img_1.jpeg](Lec4_images/page_25_img_1.jpeg)


---

## Page 26

0 Darolm 0 My first React appl Welcome :) Name: Ryu Age: 30 Belt: black Name: Crystal Age: 25 Belt: pink Name; Age: Belt: Submit

*(Extracted via OCR)*


### Images:

![page_26_img_1.jpeg](Lec4_images/page_26_img_1.jpeg)


---

## Page 27

M4tc #Fp punok Jo Elements Sources Console X My first React appl Filter Default levels Groy Welcome :) Name: Ryu Age: 30 Belt: black Name: Crystal Age: 25 [Belt: pink Name: yoshi Age: 40 Belt: orange Submit Consale What's New * Sensors Highlights from the Chrome 67 update Search across all network headers Press Control Fin the Network panel t0 open the Network Search pane: CSS variable value previews in the Styles pane When pfobemu Value iS CSS variable Deulools top

*(Extracted via OCR)*


### Images:

![page_27_img_1.png](Lec4_images/page_27_img_1.png)


---

## Page 28

ip 0 Oanolt IGa Elements Sources Console My first React appl Filter Default levels Grou 8 AddNinja_Jsile Welcome :) {name: "yoshi age: "40 belt: "orange Name: Ryu Age: 30 BBelt: black Name; Crystal Age: 25 BBelt: pink Name: yoshi Age:40 Belt: orange Submit Cansale What's New Sensors Highlights from the Chrome 67 update Search across all network headers Press Control Fin the Network panel t0 open the Network Search pane: CSS variable value previews in the Styles pane When pfobemu Value iS CSS variable Devlools top

*(Extracted via OCR)*


### Images:

![page_28_img_1.png](Lec4_images/page_28_img_1.png)


---

## Page 29

Now what we need:
We need to add the stuff which we got in the last slide from the user to the nijas list 
which we mentioned in the start.
But how?


---

## Page 30

FUNCTIONS AS PROPS

FUNCTIONS AS PROPS

*(Extracted via OCR)*


---

## Page 31

BAC Apon Hanan Ortnictom anaa inport React , Component }from react 0 Arok Aptte Inpor t Ninjas from INinjas ANa RAcnDurcounn inport AddNinja fron /AddNinja pp node nedule class App extends Component stote Jate Lco ninjas [ Anerhtnl antelon namc Ryu age : 30 belt 'black id 1 % name . 'Yoshi age 20 , belt: green" Ida 2 %, addnenia je 10 name Crystal age 25, belt: pink id: 3 } Kppn 11 Inert 12 Jnk Nintatn a addNinja (ninja) TcgistersenceNolek le pient 1S packag todyan 16 render() padarron FEADMAnd 47 return 18 div classNarc-"App 9 <hlMy first React appl</hl> 3a SNclcone 2 72 Ninjas ninjas-[thisstate ninjas 22 AdaNinjo Dubk

*(Extracted via OCR)*


### Images:

![page_31_img_1.jpeg](Lec4_images/page_31_img_1.jpeg)


---

## Page 32

EACE ppa atNtin ortmtonom Kaeto Inpont React , Component } from react 0 Aepr Mcc Inpor t Ninjas From INinjas ANinan inport AddNinja fron [AddNinja HAcEMDUXtotru 8 Mapp oocnedule class App extends Component { Dubic state Hatconco ninjas [ Hnethtl anf eLjc namc 'Ryu" JgC :   30, belt 'black Id1 % name Yoshi age : 20 belt: green id 2 %, Addreniaje 10 name Crystal age 25 belt : pink Id: 3 } Appn 11 Hctan 12 Hnatn Nniatn 43 addNinja (ninja) TcgisterScncetolie F la Dloioe 1s packaae lotyan 16 render() padataron FPEALMAnd D return 18 Idiv classNarer App 9 <hlMy first React appl</hls K) SNclcome Ueln Fa Ninjas ninjas-Ithis state ninjas 22 AddNinjo addNinjarithis addNinjal

*(Extracted via OCR)*


### Images:

![page_32_img_1.jpeg](Lec4_images/page_32_img_1.jpeg)


---

## Page 33

Calling a func and passing a ninja obj through state


### Images:

![page_33_img_1.jpeg](Lec4_images/page_33_img_1.jpeg)


---

## Page 34

Enoat pof L Onntonons Import React , Component fron react O cok ua inport Ninjas from /Ninjas oaNinu Inpor t AdNinja from /AddNinja HACI MDUXcorLIt app obl madula 5 class App extends Component publc Istate Jkonto ninjas Hinicant muanteujon name Ryu age: 30 belt: black Id; 1 %, name 'Yoshi abe 20, belt: green' id: 2 }, ddrenkajs 10 name Crystal age: 25 , belt: pink Id: 3 } Appk uracer 11 Andete Ninktk a addNinja (ninja) Teoise Scrnccholctn 1a console.log(ninjal: oionce 19 ninje (parancter) ninja: any Dadet-lodhkien 16 render() ninja oadatanon PEADHAid a ceturn Ninjas 18 div classhanes addNinja 9 <hi>My first Add a SWclcome add inj 71 <Ninjas ninjas= this state ninjas F AddNinja addNinja (this addNinja MNinja

*(Extracted via OCR)*


### Images:

![page_34_img_1.jpeg](Lec4_images/page_34_img_1.jpeg)


---

## Page 35

d4 0 Elements sourcos Console 0 first React appl top Filtae Delault Hevels Grou APp_Jsil4 Welcome :) (name: "mario age: 740 belt: "blacr Name: Ryu Age: 30 BBelt; black Name: Crystal Age; 25 Belt: pink Name: mjio Age: 40 Belt: black Submt My

*(Extracted via OCR)*


### Images:

![page_35_img_1.png](Lec4_images/page_35_img_1.png)


---

## Page 36

Adding id in ninja obj as we are not interested to take it from user


### Images:

![page_36_img_1.jpeg](Lec4_images/page_36_img_1.jpeg)


---

## Page 37

Not do this already updating array what of setState


### Images:

![page_37_img_1.jpeg](Lec4_images/page_37_img_1.jpeg)


---

## Page 38

Do not alter the state without setState

Do not alter the state without setState

*(Extracted via OCR)*


---

## Page 39

Generate a copy

OACAA Apoj anofen orntoton Inpor + React , Component Tron react 0 inpor t Ninjas from INinjas Koo Ninior Iytntvt HACMDUK CDMHLL impor t AddNinja fron [AddNinja Tot rodule class App extends Component publs state Haukonico ninjas [ ienaeml ani Ac {Kname : Ryu" age :  30 belt : 'black Id: 1 }, name Yoshi age : 20 , belt id: 2 }, addreniajs 18 name Crystal age 25 , belt : pink Id: 3 } Ed m maan 12 indcrk Ninatn 1J addNinja (ninja) egistc Sercerorcr J4 ninja id Math random() Oience 115 let ninja this state ninjas ] padgHodjan 16 this setState( { Dachenon FEADMEmd 17 ninjas : 18 419 20 rendcr ( ) 4 Feturn {12 dlv classNanee"App 2 <hiSMy first React appkk/hla 2 >Welcome l 75 <Ninjos ninjas-(this state ninjas Generate a copy 'green"

*(Extracted via OCR)*


### Images:

![page_39_img_1.jpeg](Lec4_images/page_39_img_1.jpeg)


---

## Page 40

<!DOCTYPE html>
<html>
<body>
<script>
const numbers = [1, 2, 3, 4, 5, 6];
const [one, two, ...rest] = numbers;
document.write("<p>" + one + "</p>");
document.write("<p>" + two + "</p>");
document.write("<p>" + rest + "</p>");
</script>
</body>
</html>


---

## Page 41

EnCT Apoj HaNtn ortntoton Ia Impor + React , {Component Trom react 0 Acor Inport Ninjas from INinjas Aaninan HInport AddNinja fron [AddNinja FEACTRIDUX CONTLET Iepp madule 5 class App extends Component publlc state Iakenco ninjas [ Hlan neml muantaten name Ryu age 30 belt black' id:1 } name Yoshi 'age : 20 belt id; 2 %, Addrenja | 10 name Crystal age : 25, belt : pink Id: 3 } Lapa jt 01 And 2 Jnden Ninkatk D9 addNinja (ninja) Icoistersenvce  orkcrn 14 ninja id Math random() oience 15 let ninjas this state ninjas, ninja]; Dacage lodyjion 16 this setStatel { pacanon PEADAAnd 17 ninjas ninjas 18 19 0 render() 1 ceturn K Kdiv classNangs"App odn green"

*(Extracted via OCR)*


### Images:

![page_41_img_1.jpeg](Lec4_images/page_41_img_1.jpeg)


---

## Page 42

0 Kaeen eeie Elements Sources Console X 0 My first React appl top Filter Default levels 8 Welcome :) Name: Ryu Age: 30 Belt; black Name: Crystal Age: 25 Belt: pink Name; marlo Age: 35 BBelt; black Name matio Age. 35 Belt: bblach Subm Groi

*(Extracted via OCR)*


### Images:

![page_42_img_1.png](Lec4_images/page_42_img_1.png)


---

## Page 43

Add delete Ninja functionality in current code

Add delete Ninja functionality in current code

*(Extracted via OCR)*


---

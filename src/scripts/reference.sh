#!/bin/bash


#All this script will only apply to the ref module because the tutorial module does not seen to have any xrefs in it


#Replace the xrefs for internal references
sed -i 's/xref:.*\]/&>>/' emilua/doc/modules/ref/pages/*.adoc 
sed -i 's/xref:/<<_/' emilua/doc/modules/ref/pages/*.adoc


#appending the , inherent for the reference and exchange filename for section ID
sed -i 's/.adoc/&,/' emilua/doc/modules/ref/pages/*.adoc
sed -i 's/.adoc//g' emilua/doc/modules/ref/pages/*.adoc

#perl ATR REGEX code using the lookaround match
perl -pi -e 's/(?<=,)\[//' emilua/doc/modules/ref/pages/*.adoc
perl -pi -e 's/\](?=\>)//' emilua/doc/modules/ref/pages/*.adoc 
perl -pi -e 's/(<<_[A-Za-z]+)\./\1_/g' emilua/doc/modules/ref/pages/*.adoc






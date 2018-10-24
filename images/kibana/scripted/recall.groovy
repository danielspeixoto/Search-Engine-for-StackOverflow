def total = 0;
for(def i = 0; i < doc['retrieved'].length; i++) {
    for(def j = 0; j < doc['expected'].length; j++) {
        if(doc['retrieved'][i]  == doc['expected'][j]) {
            total++;
        }
    }
}
return total / doc['expected'].length;
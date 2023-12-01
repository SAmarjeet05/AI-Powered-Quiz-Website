const dictionary_nested_list =[{1: ' D) Operational Amplifier', 2: ' C) Operative Amplification', 3: ' B) Operational Amplification', 4: ' A) Operating Amplifier', 5: '1. In an op-amp circuit, what does "op-amp" stand for?'}, {1: ' D) None of the above', 2: ' C) Both inputs are labeled with positive signs', 3: ' B) Inverting input', 4: ' A) Non-inverting input', 5: '2. Which input of an op-amp is typically labeled with a positive sign?'}, {1: ' D) It depends on the specific op-amp circuit', 2: ' C) 0', 3: ' B) Infinity', 4: ' A) 1', 5: '3. What is the ideal voltage gain of an op-amp?'}]
const myobject = {firstname:"Amarjeet",lastname:"Singh"}

let details = [];
        
for (let i=0; i<dictionary_nested_list.length;i++){
    //console.log(dictionary_nested_list[i]);
    const dictionaries = dictionary_nested_list[i]
    for (key in dictionaries){
        console.log(dictionaries[key]);
        details.push(dictionaries[key])
    }
}

console.log(details)
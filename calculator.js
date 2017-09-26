function percentXInput(oddslist){
	let sum = 0;
	for(let i = 0; i < oddslist.length; i++){
		if(oddslist[i] > 0){
			let percent = (1/oddslist[i])*100;
			sum = sum + percent; 
		}
	}
	return sum;
}

function percentOutcome(oddslist){
	let sum = percentXInput(oddslist);
	let profit = (100/sum)*100;
	return profit;
}

function rawProfitPercent(oddslist){
	let percent = percentOutcome(oddslist);
	let raw = (percent - 100);
	return raw;
}

function rawProfit(oddslist, capital){
	let raw_profit_percent = rawProfitPercent(oddslist);
	return ((raw_profit_percent/100)*capital).toFixed(2);
}

function fractionToDecimal(fraction){
	let strspl = fraction.split("/");

	let intlist = [];

	for(let i = 0; i < strspl.length; i++){ 
		intlist.push(parseInt(strspl[i]));
	}


	let decimal = 1 + (intlist[0]/intlist[1])
	return decimal;
}

function americanToDecimal(american){
	
	let decimal = 0

	if (american > 0){
		decimal = (american/100) + 1;
	}
	else{
		decimal = (100/american) + 1;
	}

	return decimal;
}	

function maxProfitValuesX(oddslist,capital){
	let percentlist = [];

	let sum = 0

	for(let i = 0; i < oddslist.length; i++){
		if(oddslist[i] > 0){
			let percent = (1/oddslist[i])*100;
			percentlist.push(percent);
			sum = sum + percent;
		}else{
			percentlist.push(0);
		}
	}
	let betlist = [];

	for(let i = 0; i < percentlist.length; i++){
		let bet = (capital*percentlist[i])/sum;
		betlist.push(bet.toFixed(2));
	}
	return betlist;
}


function changeSystem(){
	let system = document.getElementById("systemselect").value;
	if(system === "Fractional"){
		for(let i = 0; i < 6; i++){
			document.getElementById("odds" + i).type = "text";
			document.getElementById("odds" + i).size = "9";
			document.getElementById("odds" + i).value = "0";
			document.getElementById("bet" + i).value = "0.00";		
		}
	}else if(system === "Decimal"){
		for(let i = 0; i < 6; i++){
			document.getElementById("odds" + i).type = "number";
			document.getElementById("odds" + i).value = "0.00";
			document.getElementById("bet" + i).value = "0.00";	
		}
	}else if(system === "American"){
		for(let i = 0; i < 6; i++){
			document.getElementById("odds" + i).type = "number";
			document.getElementById("odds" + i).value = "0";
			document.getElementById("bet" + i).value = "0.00";	
		}
	}
	document.getElementById("profitpercent").innerHTML = "0%";
	document.getElementById("rawprofit").innerHTML = "$0.00";
}

function convertToDecimal(oddslist,system){

	if(system === "Fractional"){
		for(let i = 0; i < oddslist.length; i++){
			oddslist[i] = fractionToDecimal(oddslist[i]);
		}
	}else if(system ==="American"){
		for(let i = 0; i < oddslist.length; i++){
			oddslist[i] = americanToDecimal(oddslist[i]);
		}
	}
}

function profitColor(profitPercent){
	console.log(profitPercent);
	if(profitPercent > 2){
		document.getElementById("profitpercent").style.color = "green";
	}else if(2 > profitPercent && profitPercent > 0){
		document.getElementById("profitpercent").style.color = "yellow";
	}else if(profitPercent < 0){
		document.getElementById("profitpercent").style.color = "red";
	}
}

function noneZeros(list){
	let count = 0;
	for(let i = 0; i < list.length; i++){
		if(list[i] > 0){
			count++
		}else{
		}
	}

	return count;
}


function outputBets(){

	let system = document.getElementById("systemselect").value;

	let oddslist = [];

	for(let i = 0; i < 6; i++){
		let odds = document.getElementById("odds" + i).value;
		oddslist.push(odds);
	}

	convertToDecimal(oddslist,system);

	let capital = document.getElementById("capital").value;
	let betlist = maxProfitValuesX(oddslist,capital);
	let profitPercent = rawProfitPercent(oddslist);
	let raw_profit = rawProfit(oddslist,capital);

	for(let i = 0; i < 6; i++){
		if(noneZeros(betlist) > 1){
			document.getElementById("bet" + i).value = betlist[i];

		}else{
			document.getElementById("bet" + i).value = "0.00";
		}
	}
	if(noneZeros(betlist)>1){
		document.getElementById("profitpercent").innerHTML = "" + profitPercent.toFixed(2) + "%";
		profitColor(profitPercent);
		document.getElementById("rawprofit").innerHTML = "$" + raw_profit;
	}
	
}






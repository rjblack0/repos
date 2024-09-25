string centerText(string text, int length, char fill = ' ') {

    int textLength = text.length(); //get the length of the text to be centered
    string centeredText = ""; //stores final version of text with padding

    if (textLength >= length) {
        return text;
    }//if (textLength >= length)
    else {
        int charsNeeded = (length - textLength); //how many characters are need to fill on left and right
        int paddingNeeded = (charsNeeded / 2); //calculate the number of padding characters needed
        string leftPadding = string(paddingNeeded, fill);
        string rightPadding = leftPadding;
        centeredText = (leftPadding + text + rightPadding);


        if (charsNeeded % 2 != 0) { // check if need an additional character to make sure centered text length 
            centeredText.insert(0, 1, fill);
    return (centeredText);
    }//else

} //center text
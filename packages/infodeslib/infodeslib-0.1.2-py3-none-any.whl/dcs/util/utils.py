

def soft_vote_predictions(predictions, plot): 
    num_modalities = len(predictions)
    num_classes    = len(predictions[0]) 
    
    classes_preds = []
    probs = [] 
    conf_list = []  
    
    for i in range(num_classes): 
        classes_preds.append([]) 
 
    for i in range(num_modalities):    
        for j in range(num_classes): 
            classes_preds[j].append(predictions[i][j]) 
    
    for c in range(num_classes): 
        probs.append(sum(classes_preds[c])) 
    
    for p in probs: 
        conf_list.append(round(p / num_modalities * 100, 2))
    
    ## *** prediction *** ## 
    prediction = probs.index(max(probs)) 
    conf = round(max(probs) / num_modalities * 100, 2)
    
    if plot: 
        print("[Prediction]: {} (Confidence: {} %)".format(prediction, conf)) 

    return prediction, conf, conf_list 


def make_table_highlights(styler, title):
    styler.set_caption(title)
    styler.background_gradient(axis=0, cmap="YlOrBr")
    return styler
peaks_list=[0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]

most_peaks_list=[peaks_list[0],peaks_list[1]]

updated_peaks_list_smaller =[]

updated_peaks_list_bigger=[]

length_dictionary={}

def next_peak_check(current_route_list, peak_index):
    updated_peaks_list_smaller=current_route_list[:]
    updated_peaks_list_bigger=current_route_list[:]

    if peak_index==len(peaks_list):
        length_dictionary[len(current_route_list)]=current_route_list
        return 

    #Smaller Check
    if peaks_list[peak_index] < updated_peaks_list_smaller[-1]:
        for i in range(0, len(current_route_list)):
            updated_peaks_list_smaller=current_route_list[0:i+1]
            if peaks_list[peak_index] < updated_peaks_list_smaller[-1]:
                updated_peaks_list_smaller=updated_peaks_list_smaller[0:i]
                updated_peaks_list_smaller.append(peaks_list[peak_index])
                break
        bigger_or_smaller = next_peak_check(updated_peaks_list_smaller, peak_index+1)

  
    #Bigger Check
    if peaks_list[peak_index] > updated_peaks_list_bigger[-1]:
        updated_peaks_list_bigger.append(peaks_list[peak_index])
        next_peak_check(updated_peaks_list_bigger, peak_index+1)

    next_peak_check(current_route_list, peak_index+1)

next_peak_check(most_peaks_list,2)            

print(length_dictionary[max(length_dictionary)])
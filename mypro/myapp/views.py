from django.shortcuts import render

def power(request):
    context = {'P': "0", 'I': "0", 'R': "0"}
    if request.method == 'POST':
        print("POST method is used")
        I = request.POST.get('Current', '0')
        R = request.POST.get('Resistance', '0')
        print('Current =', I)
        print('Resistance =', R)
        try:
            I_val = float(I)
            R_val = float(R)
            P = I_val * I_val * R_val   # Formula: P = I² * R
            context['P'] = round(P, 2)
            context['I'] = I
            context['R'] = R
            print('Power =', P)
        except ValueError:
            context['P'] = "Invalid Input"
    return render(request, 'myapp/power.html', context)
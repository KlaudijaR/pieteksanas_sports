def treneris_f(treneri_v,paroles,treneris_apraksts,zvaigznes,treneris_pieejams): #definē funkciju
   turpinat=("jā")
   jautajumi=("nē")
   while turpinat==("jā"): 
      v_parbaud=str(input("Ievadat savu vārdu un uzvārdu: ")) #treneris ievada savu vārdu un uzvārdu
      pin_parbaud=str(input("Ievadi savu paroli: ")) #treneris ievada savu paroli
      for i in range(len(treneri_v)):
        if v_parbaud==treneri_v[i] and pin_parbaud==paroles[i]: #pārbauda vai ievadītie dati pareizi
          print("Sveiki teneri-e!") 
          while jautajumi!=("jā"):
            jautajumi=int(input("Ko gribat darīt?\n 1.pārmainīt savu aprakstu\n 2.pārmainīt darbadienas un laikus\n 3.apskatīt savus reitingus (rakstat ar cipariem): ")) #jautā ko vēlas darīt
            if jautajumi==(1): #ja izvēlas 1
              apraksts_main=str(input("Rakstat pilnu aprakstu ar jūsu gribētājām pārmaiņām: ")) # var ievadīt sev vēlamo aprakstu
              treneris_apraksts[i]=apraksts_main
            if jautajumi==(2): #ja izvēlas 2
              pieejams_main=str(input("Ievadiet savus pārmainītos darba laikus, dienas: ")) #dod iespēju mainīt savus darba laikus un dienas
              treneris_pieejams[i]=pieejams_main #maina šos darba laikus
            if jautajumi==(3): #ja izvēlas 3
              print(zvaigznes[i]) #parāda viņu reitingu
            jautajumi=str(input("vai gribi iziet? ")) 
            turpinat=("nē")
          break
        elif i==len(paroles)-1: #pārbauda vai parole ir pareiza
          print("Nepareizs vārds, vai parole.") 
          turpinat=str(input("vai mēģināsiet velreiz?: "))#atļauj lietotājam ievadīt datus velreiz
          break
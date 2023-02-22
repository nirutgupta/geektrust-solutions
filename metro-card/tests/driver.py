from src.service.metro_service import MetroService
ms = MetroService()

"""

BALANCEMC1 600
BALANCEMC2 500 
BALANCEMC3 50 
BALANCEMC4 50 
BALANCEMC5 200 
CHECK_INMC1 ADULT CENTRAL 
CHECK_INMC2 SENIOR_CITIZEN CENTRAL 
CHECK_INMC1 ADULT AIRPORT 
CHECK_INMC3 KID AIRPORT 
CHECK_INMC4 ADULT AIRPORT 
CHECK_INMC5 KID AIRPORT 
PRINT_SUMMARY 

"""
ms.init_metro_card("MC1", 600)
ms.init_metro_card("MC2", 500)
ms.init_metro_card("MC3", 50)
ms.init_metro_card("MC4", 50)
ms.init_metro_card("MC5", 200)
ms.check_in("MC1", "ADULT", "CENTRAL")
ms.check_in("MC2", "SENIOR_CITIZEN", "CENTRAL")
ms.check_in("MC1", "ADULT", "AIRPORT")
ms.check_in("MC3", "KID", "AIRPORT")
ms.check_in("MC4", "ADULT", "AIRPORT")
ms.check_in("MC5", "KID", "AIRPORT")
ms.print_summary()

"""
BALANCEMC1 400
BALANCEMC2 100 
BALANCEMC3 50 
BALANCEMC4 50
CHECK_INMC1 SENIOR_CITIZEN AIRPORT 
CHECK_INMC2 KID AIRPORT 
CHECK_INMC3 ADULT CENTRAL 
CHECK_INMC1 SENIOR_CITIZEN CENTRAL 
CHECK_INMC3 ADULT AIRPORT 
CHECK_INMC3 ADULT CENTRAL 
PRINT_SUMMARY 

"""

# ms.init_metro_card("MC1", 400)
# ms.init_metro_card("MC2", 100)
# ms.init_metro_card("MC3", 50)
# ms.init_metro_card("MC4", 50)
# ms.check_in("MC1", "SENIOR_CITIZEN", "AIRPORT")
# ms.check_in("MC2", "KID", "AIRPORT")
# ms.check_in("MC3", "ADULT", "CENTRAL")
# ms.check_in("MC1", "SENIOR_CITIZEN", "CENTRAL")
# ms.check_in("MC3", "ADULT", "AIRPORT")
# ms.check_in("MC3", "ADULT", "CENTRAL")
# ms.print_summary()

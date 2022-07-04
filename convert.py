import xml.etree.ElementTree as Xet
import pandas as pd
import datetime
import os
import os.path
import sys

def convert():

  time_start = datetime.datetime.now().replace(microsecond=0)
  
  Info_lastNm = []
  Info_firstNm = []
  Info_midNm = []
  Info_indvlPK = []
  Info_actvAGReg = []
  Info_link = []
  
  OthrNm_lastNm = []
  OthrNm_firstNm = []
  OthrNm_midNm = []
  
  CrntEmp_orgNm = []
  CrntEmp_orgPK = []
  CrntEmp_str1 = []
  CrntEmp_city = []
  CrntEmp_state = []
  CrntEmp_cntry = []
  CrntEmp_postlCd = []
  
  CrntRgstn_regAuth = []
  CrntRgstn_regCat = []
  CrntRgstn_st = []
  CrntRgstn_stDt = []
  
  BrnchOfLoc_str1 = []
  BrnchOfLoc_city = []
  BrnchOfLoc_state = []
  BrnchOfLoc_cntry = []
  BrnchOfLoc_postlCd = []

  Exm_exmCd = []
  Exm_exmNm = []
  Exm_exmDt = []

  Dsgntn_dsgntnNm = []

  PrevRgstn_orgNm = []
  PrevRgstn_orgPK = []
  PrevRgstn_regBeginDt = []
  PrevRgstn_regEndDt = []

  PrevRgstn_branchloc_city = []
  PrevRgstn_branchloc_state = []

  EmpHs_fromDt = []
  EmpHs_toDt = []
  EmpHs_orgNm = []
  EmpHs_city = []
  EmpHs_state = []

  OthrBus_desc = []

  DRP_hasRegAction = []
  DRP_hasCriminal = []
  DRP_hasBankrupt = []
  DRP_hasCivilJudc = []
  DRP_hasBond = []
  DRP_hasJudgment = []
  DRP_hasInvstgn = []
  DRP_hasCustComp = []
  DRP_hasTermination = []

  tree=Xet.parse( 'sample.xml' )
  root=tree.getroot()
  Indvls = list(root[0])
  Indvl = list(Indvls)

  for Indvl_child in Indvl:
    
    # Loop for Info Tag
    for child in Indvl_child:
      
      keys = child.attrib.keys()
      
      if len(keys) != 0:
        for k in keys:
          if k == 'lastNm':
            Info_lastNm.append(child.attrib[k] if (child.attrib[k] is not None) or (child.attrib[k] != ' ') else 'None')
            # print(f'{k}: {child.attrib[k]}\n')

          elif k == 'firstNm':
            Info_firstNm.append(child.attrib[k] if (child.attrib[k] is not None) or (child.attrib[k] != ' ') else 'None')
            #print(f'{k}: {child.attrib[k]}\n')

          elif k == 'midNm':
            Info_midNm.append(child.attrib[k] if (child.attrib[k] is not None) or (child.attrib[k] != ' ') else 'None')
            #print(f'{k}: {child.attrib[k]}\n')

          elif k == 'indvlPK':
            Info_indvlPK.append(child.attrib[k] if (child.attrib[k] is not None) or (child.attrib[k] != ' ') else 'None')
            #print(f'{k}: {child.attrib[k]}\n')

          elif k == 'actvAGReg':
            Info_actvAGReg.append(child.attrib[k] if (child.attrib[k] is not None) or (child.attrib[k] != ' ') else 'None')
            #print(f'{k}: {child.attrib[k]}\n')

          elif k == 'link':
            Info_link.append(child.attrib[k] if (child.attrib[k] is not None) or (child.attrib[k] != ' ') else 'None')
            #print(f'{k}: {child.attrib[k]}\n')

        # Check if Info attributes are complete
        if 'lastNm' in keys:
          pass
        else:
          Info_lastNm.append('None')
          #print(f'lastNm : None\n')

        if 'firstNm' in keys:
          pass
        else:
          Info_firstNm.append('None')
          #print(f'firstNm : None\n')

        if 'midNm' in keys:
          pass
        else:
          Info_midNm.append('None')
          #print(f'midNm : None\n')

        if 'indvlPK' in keys:
          pass
        else:
          Info_indvlPK.append('None')
          #print(f'indvlPK : None\n')

        if 'actvAGReg' in keys:
          pass
        else:
          Info_actvAGReg.append('None')
          #print(f'actvAGReg : None\n')

        if 'link' in keys:
          pass
        else:
          Info_link.append('None')
          #print(f'link : None\n')

    # Loop for OthrNms Tag
    OthrNms_child = list(Indvl_child[1])

    # OtherNm variables
    lastNm_all = ''
    firstNm_all = ''
    midNm_all = ''

    if len(OthrNms_child) !=0:

      for child in OthrNms_child:
        
        keys = child.attrib.keys()
        
        if len(keys) != 0:

          for k in keys:

            if k == 'lastNm':
              lastNm_all += child.attrib[k] + ',\n'
              #print(f'{k}: {child.attrib[k]}\n')

            elif k == 'firstNm':
              firstNm_all += child.attrib[k] + ',\n'
              #print(f'{k}: {child.attrib[k]}\n')

            elif k == 'midNm':
              midNm_all += child.attrib[k] + ',\n'
              #print(f'{k}: {child.attrib[k]}\n')
          
          # Check if OthrNms attributes are complete
          if 'lastNm' in keys:
            pass
          else:
            lastNm_all += 'None,\n'
            #print(f'lastNm : None\n')

          if 'firstNm' in keys:
            pass
          else:
            firstNm_all += 'None,\n'
            #print(f'firstNm : None\n')

          if 'midNm' in keys:
            pass
          else:
            midNm_all += 'None,\n'
            #print(f'firstNm : None\n')

      OthrNm_lastNm.append(lastNm_all)
      OthrNm_firstNm.append(firstNm_all)
      OthrNm_midNm.append(midNm_all)

    else:
      OthrNm_lastNm.append('None')
      OthrNm_firstNm.append('None')
      OthrNm_midNm.append('None')

    # Loop for CrntEmps Tag
    CrntEmps_child = list(Indvl_child[2])

    # CrntEmp variables
    orgNm_all = ''
    orgPK_all = ''
    str1_all = ''
    city_all = ''
    state_all = ''
    cntry_all = ''
    postlCd_all = ''

    for child in CrntEmps_child:
      
      keys = child.attrib.keys()
      
      if len(keys) != 0:
        for k in keys:

          if k == 'orgNm':
            orgNm_all += child.attrib[k] + ',\n'
            #print(f'{k}: {child.attrib[k]}\n')

          elif k == 'orgPK':
            orgPK_all += child.attrib[k] + ',\n'
            #print(f'{k}: {child.attrib[k]}\n')

          elif k == 'str1':
            str1_all += child.attrib[k] + ',\n'
            #print(f'{k}: {child.attrib[k]}\n')

          elif k == 'city':
            city_all += child.attrib[k] + ',\n'
            #print(f'{k}: {child.attrib[k]}\n')

          elif k == 'state':
            state_all += child.attrib[k] + ',\n'
            #print(f'{k}: {nodes.attrib[k]}\n')

          elif k == 'cntry':
            cntry_all += child.attrib[k] + ',\n'
            #print(f'{k}: {nodes.attrib[k]}\n')

          elif k == 'postlCd':
            postlCd_all += child.attrib[k] + ',\n'
            #print(f'{k}: {child.attrib[k]}\n')

        # Check if CrntEmp branchloc attribute is complete
        if 'orgNm' in keys:
          pass
        else:
          orgNm_all += 'None,\n'
          #print(f'orgNm : None\n')

        if 'orgPK' in keys:
          pass
        else:
          orgPK_all += 'None,\n'
          #print(f'orgPK : None\n')

        if 'str1' in keys:
          pass
        else:
          str1_all += 'None,\n'
          #print(f'str1 : None\n')

        if 'city' in keys:
          pass
        else:
          city_all += 'None,\n'
          #print(f'city : None\n')

        if 'state' in keys:
          pass
        else:
          state_all += 'None,\n'
          #print(f'state : None\n')

        if 'cntry' in keys:
          pass
        else:
          cntry_all += 'None,\n'
          #print(f'cntry : None\n')

        if 'postlCd' in keys:
          pass
        else:
          postlCd_all += 'None,\n'
          #print(f'postlCd : None\n')
          
    CrntEmp_orgNm.append(orgNm_all)
    CrntEmp_orgPK.append(orgPK_all)
    CrntEmp_str1.append(str1_all)
    CrntEmp_city.append(city_all)
    CrntEmp_state.append(state_all)
    CrntEmp_cntry.append(cntry_all)
    CrntEmp_postlCd.append(postlCd_all)

    # CrntRgstn variables
    regAuth_all = ''
    regCat_all = ''
    st_all = ''
    stDt_all = ''

    # BrnchOfLoc variables
    str1_all = ''
    city_all = ''
    state_all = ''
    cntry_all = ''
    postlCd_all = ''

    # Loop for CrntEmps CrntRgstn tag
    CrntRgstn = list(CrntEmps_child)

    CrntRgstn_child = list(CrntRgstn)

    for child in CrntRgstn_child:

      nodes = list(child)

      for node in nodes:

        for item in node:

          keys = item.attrib.keys()
          print(keys)

          for k in keys:
            if k == 'regAuth':
              regAuth_all += item.attrib[k] + ',\n'
              # print(f'{k}: {child.attrib[k]}\n')

            elif k == 'regCat':
              regCat_all += item.attrib[k] + ',\n'
              # print(f'{k}: {item.attrib[k]}\n')

            elif k == 'st':
              st_all += item.attrib[k] + ',\n'
              # print(f'{k}: {item.attrib[k]}\n')

            elif k == 'stDt':
              stDt_all += item.attrib[k] + ',\n'
              # print(f'{k}: {item.attrib[k]}\n')

    CrntRgstn_regAuth.append(regAuth_all)
    CrntRgstn_regCat.append(regCat_all)
    CrntRgstn_st.append(st_all)
    CrntRgstn_stDt.append(stDt_all)

    # Loop for CrntEmps BrnchOfLocs tag
    BrnchOfLocs = list(CrntEmps_child)

    BrnchOfLocs_child = list(BrnchOfLocs)

    for child in BrnchOfLocs_child:

      nodes = list(child)

      for node in nodes:

        for item in node:

          keys = item.attrib.keys()

          for k in keys:
            if 'regAuth' in keys:
              pass
            else:
              if k == 'str1':
                str1_all += item.attrib[k] + ',\n'
                # print(f'{k}: {child.attrib[k]}\n')

              elif k == 'city':
                city_all += item.attrib[k] + ',\n'
                # print(f'{k}: {item.attrib[k]}\n')

              elif k == 'state':
                state_all += item.attrib[k] + ',\n'
                # print(f'{k}: {item.attrib[k]}\n')

              elif k == 'cntry':
                cntry_all += item.attrib[k] + ',\n'
                # print(f'{k}: {item.attrib[k]}\n')

              elif k == 'postlCd':
                postlCd_all += item.attrib[k] + ',\n'
                # print(f'{k}: {item.attrib[k]}\n')

    BrnchOfLoc_str1.append(regAuth_all)
    BrnchOfLoc_city.append(regCat_all)
    BrnchOfLoc_state.append(st_all)
    BrnchOfLoc_cntry.append(stDt_all)
    BrnchOfLoc_postlCd.append(stDt_all)

    # Loop for Exms Tag
    Exms = list(Indvl_child[3])

    # Exm variables
    exmCd_all = ''
    exmNm_all = ''
    exmDt_all = ''

    if len(Exms) != 0:

      for child in Exms:
        
        keys = child.attrib.keys()
        
        if len(keys) != 0:
          for k in keys:
            if k == 'exmCd':
              exmCd_all += child.attrib[k] + ',\n'
              #print(f'{k}: {child.attrib[k]}\n')

            elif k == 'exmNm':
              exmNm_all += child.attrib[k] + ',\n'
              #print(f'{k}: {child.attrib[k]}\n')

            elif k == 'exmDt':
              exmDt_all += child.attrib[k] + ',\n'
              #print(f'{k}: {child.attrib[k]}\n')

      Exm_exmCd.append(exmCd_all)
      Exm_exmNm.append(exmNm_all)
      Exm_exmDt.append(exmDt_all)

    else:
      Exm_exmCd.append('None')
      Exm_exmNm.append('None')
      Exm_exmDt.append('None')

    # Loop for Dsgntn Tag
    Dsgntn = list(Indvl_child[4])
    
    if len(Dsgntn) != 0:
      for child in Dsgntn:
        
        keys = child.attrib.keys()
        
        if len(keys) != 0:
          for k in keys:
            if k == 'dsgntnNm':
              Dsgntn_dsgntnNm.append(child.attrib[k] if (child.attrib[k] is not None) or (child.attrib[k] != ' ') else 'None')
              #print(f'{k}: {child.attrib[k]}\n')
    else:
      Dsgntn_dsgntnNm.append('None')
    
    # Loop for PrevRgstns Tag
    PrevRgstns = list(Indvl_child[5])

    # PrevRgstn variables
    orgNm_all = ''
    orgPK_all = ''
    regBeginDt_all = ''
    regEndDt_all = ''

    if len(PrevRgstns) != 0:
      
      for child in PrevRgstns:
        
        keys = child.attrib.keys()
        
        if len(keys) != 0:
          for k in keys:
            if k == 'orgNm':
              orgNm_all += child.attrib[k] + ',\n'
              #print(f'{k}: {child.attrib[k]}\n')

            elif k == 'orgPK':
              orgPK_all += child.attrib[k] + ',\n'
              #print(f'{k}: {child.attrib[k]}\n')

            elif k == 'regBeginDt':
              regBeginDt_all += child.attrib[k] + ',\n'
              #print(f'{k}: {child.attrib[k]}\n')

            elif k == 'regEndDt':
              regEndDt_all += child.attrib[k] + ',\n'
              #print(f'{k}: {child.attrib[k]}\n')

        # Loop for PrevRgstn_branchloc Tag
        PrevRgstn_branchloc = list(child)

        PrevRgstn_branchloc_nodes = list(PrevRgstn_branchloc)

        # PrevRgstn BrnchOfLoc variables
        city_all = ''
        state_all = ''

        if len(PrevRgstn_branchloc_nodes) != 0:

          for node in PrevRgstn_branchloc_nodes:

            items = list(node)

            for item in items:
            
              keys = item.attrib.keys()

              if len(keys) != 0:
                for k in keys:
                  if k == 'city':
                    city_all += item.attrib[k] + ',\n'
                    #print(f'{k}: {item.attrib[k]}\n')

                  elif k == 'state':
                    state_all += item.attrib[k] + ',\n'
                    #print(f'{k}: {item.attrib[k]}\n')

        else:
          PrevRgstn_branchloc_city.append('None')
          PrevRgstn_branchloc_state.append('None')

      PrevRgstn_orgNm.append(orgNm_all)
      PrevRgstn_orgPK.append(orgPK_all)
      PrevRgstn_regBeginDt.append(regBeginDt_all)
      PrevRgstn_regEndDt.append(regEndDt_all)

      PrevRgstn_branchloc_city.append(city_all)
      PrevRgstn_branchloc_state.append(state_all)

    else:
      PrevRgstn_orgNm.append('None')
      PrevRgstn_orgPK.append('None')
      PrevRgstn_regBeginDt.append('None')
      PrevRgstn_regEndDt.append('None')
  
    # Loop for PrevRgstns Tag
    EmpHss = list(Indvl_child[6])

    # EmpHs variables
    EmpHs_fromDt_all = ''
    EmpHs_toDt_all = ''
    EmpHs_orgNm_all = ''
    EmpHs_city_all = ''
    EmpHs_state_all = ''

    if len(EmpHss) != 0:
      for child in EmpHss:
        
        keys = child.attrib.keys()

        if len(keys) != 0:
          for k in keys:
            if k == 'fromDt':
              EmpHs_fromDt_all += child.attrib[k] + ',\n'
              #print(f'{k}: {child.attrib[k]}\n')

            elif k == 'toDt':
              EmpHs_toDt_all += child.attrib[k] + ',\n'
              #print(f'{k}: {child.attrib[k]}\n')

            elif k == 'orgNm':
              EmpHs_orgNm_all += child.attrib[k] + ',\n'
              #print(f'{k}: {child.attrib[k]}\n')

            elif k == 'city':
              EmpHs_city_all += child.attrib[k] + ',\n'
              #print(f'{k}: {child.attrib[k]}\n')

            elif k == 'state':
              EmpHs_state_all += child.attrib[k] + ',\n'
              #print(f'{k}: {child.attrib[k]}\n')

          # Check if attribute toDt exist
          if 'toDt' in keys:
            pass
          else:
            EmpHs_toDt_all += 'None,\n'
            #print(f'toDt : None \n')

      EmpHs_fromDt.append(EmpHs_fromDt_all)
      EmpHs_toDt.append(EmpHs_toDt_all)
      EmpHs_orgNm.append(EmpHs_orgNm_all)
      EmpHs_city.append(EmpHs_city_all)
      EmpHs_state.append(EmpHs_state_all)

    else:
      EmpHs_fromDt.append('None')
      EmpHs_toDt.append('None')
      EmpHs_orgNm.append('None')
      EmpHs_city.append('None')
      EmpHs_state.append('None')

    # Loop for OthrBus Tag
    OthrBuss = list(Indvl_child[7])
    if len(OthrBuss) != 0:
      for child in OthrBuss:
        
        keys = child.attrib.keys()
        
        if len(keys) != 0:
          for k in keys:
            if k == 'desc':
              OthrBus_desc.append(child.attrib[k] if (child.attrib[k] is not None) or (child.attrib[k] != ' ') else 'None')
              #print(f'{k}: {child.attrib[k]}\n')
    else:
      OthrBus_desc.append('None')

    # Loop for DRP Tag
    DRP = list(Indvl_child[8])

    if len(DRP) != 0:
      for child in DRP:
        
        keys = child.attrib.keys()
        
        if len(keys) != 0:
          for k in keys:
            if k == 'hasRegAction':
              DRP_hasRegAction.append(child.attrib[k] if (child.attrib[k] is not None) or (child.attrib[k] != ' ') else 'None')
              #print(f'{k}: {child.attrib[k]}\n')

            elif k == 'hasCriminal':
              DRP_hasCriminal.append(child.attrib[k] if (child.attrib[k] is not None) or (child.attrib[k] != ' ') else 'None')
              #print(f'{k}: {child.attrib[k]}\n')

            elif k == 'hasBankrupt':
              DRP_hasBankrupt.append(child.attrib[k] if (child.attrib[k] is not None) or (child.attrib[k] != ' ') else 'None')
              #print(f'{k}: {child.attrib[k]}\n')

            elif k == 'hasCivilJudc':
              DRP_hasCivilJudc.append(child.attrib[k] if (child.attrib[k] is not None) or (child.attrib[k] != ' ') else 'None')
              #print(f'{k}: {child.attrib[k]}\n')

            elif k == 'hasBond':
              DRP_hasBond.append(child.attrib[k] if (child.attrib[k] is not None) or (child.attrib[k] != ' ') else 'None')
              #print(f'{k}: {child.attrib[k]}\n')

            elif k == 'hasJudgment':
              DRP_hasJudgment.append(child.attrib[k] if (child.attrib[k] is not None) or (child.attrib[k] != ' ') else 'None')
              #print(f'{k}: {child.attrib[k]}\n')

            elif k == 'hasInvstgn':
              DRP_hasInvstgn.append(child.attrib[k] if (child.attrib[k] is not None) or (child.attrib[k] != ' ') else 'None')
              #print(f'{k}: {child.attrib[k]}\n')

            elif k == 'hasCustComp':
              DRP_hasCustComp.append(child.attrib[k] if (child.attrib[k] is not None) or (child.attrib[k] != ' ') else 'None')
              #print(f'{k}: {child.attrib[k]}\n')

            elif k == 'hasTermination':
              DRP_hasTermination.append(child.attrib[k] if (child.attrib[k] is not None) or (child.attrib[k] != ' ') else 'None')
              #print(f'{k}: {child.attrib[k]}\n')
    else:
      DRP_hasRegAction.append('None')
      DRP_hasCriminal.append('None')
      DRP_hasBankrupt.append('None')
      DRP_hasCivilJudc.append('None')
      DRP_hasBond.append('None')
      DRP_hasJudgment.append('None')
      DRP_hasInvstgn.append('None')
      DRP_hasCustComp.append('None')
      DRP_hasTermination.append('None')
      
  time_end = datetime.datetime.now().replace(microsecond=0)
  runtime = time_end - time_start
  print(f"Script runtime: {runtime}.")

  # Save scraped URLs to a CSV file
  now = datetime.datetime.now().strftime('%Y%m%d-%Hh%M')
  print('Saving to a CSV file...')

  data = {'lastNm': Info_lastNm, 'firstNm': Info_firstNm, 'midNm': Info_midNm, 'indvlPK': Info_indvlPK, 'actvAGReg': Info_actvAGReg, 'link': Info_link, 'OthrNm lastNm': OthrNm_lastNm, 'OthrNm firstNm': OthrNm_firstNm, 'OthrNm midNm': OthrNm_midNm, 'CrntEmp orgNm': CrntEmp_orgNm, 'CrntEmp orgPK': CrntEmp_orgPK, 'CrntEmp str1': CrntEmp_str1, 'CrntEmp city': CrntEmp_city, 'CrntEmp state': CrntEmp_state, 'CrntEmp cntry': CrntEmp_cntry, 'CrntEmp postlCd': CrntEmp_postlCd, 'CrntRgstn regAuth': CrntRgstn_regAuth, 'CrntRgstn regCat': CrntRgstn_regCat, 'CrntRgstn st': CrntRgstn_st, 'CrntRgstn stDt': CrntRgstn_stDt, 'BrnchOfLoc str1': BrnchOfLoc_str1, 'BrnchOfLoc city': BrnchOfLoc_city, 'BrnchOfLoc state': BrnchOfLoc_state, 'BrnchOfLoc cntry': BrnchOfLoc_cntry, 'BrnchOfLoc postlCd': BrnchOfLoc_postlCd, 'exmCd': Exm_exmCd, 'exmNm': Exm_exmNm, 'exmDt': Exm_exmDt, 'dsgntnNm': Dsgntn_dsgntnNm, 'PrevRgstn_orgNm': PrevRgstn_orgNm, 'PrevRgstn orgPK': PrevRgstn_orgPK, 'PrevRgstn regBeginDt': PrevRgstn_regBeginDt, 'PrevRgstn regEndDt': PrevRgstn_regEndDt, 'PrevRgstn branchloc city': PrevRgstn_branchloc_city, 'PrevRgstn branchloc state': PrevRgstn_branchloc_state, 'EmpHs fromDt': EmpHs_fromDt, 'EmpHs toDt': EmpHs_toDt, 'EmpHs orgNm': EmpHs_orgNm, 'EmpHs city': EmpHs_city, 'EmpHs state': EmpHs_state, 'OthrBus desc': OthrBus_desc, 'DRP hasRegAction': DRP_hasRegAction, 'DRP hasCriminal': DRP_hasCriminal, 'DRP hasBankrupt': DRP_hasBankrupt, 'DRP hasCivilJudc': DRP_hasCivilJudc, 'DRP hasBond': DRP_hasBond, 'DRP hasJudgment': DRP_hasJudgment, 'DRP hasInvstgn': DRP_hasInvstgn, 'DRP hasCustComp': DRP_hasCustComp, 'DRP hasTermination': DRP_hasTermination}

  df=pd.DataFrame(data=data)
  df.index+=1
  directory = os.path.dirname(os.path.realpath(__file__))
  filename = "convertedXML" + now + ".csv"
  file_path = os.path.join(directory,'csvfiles/', filename)
  df.to_csv(file_path)

  print('Your files are ready.')

if __name__ == '__main__':
  convert()
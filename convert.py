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

  # Exm variables
  exmCd_all = ''
  exmNm_all = ''
  exmDt_all = ''

  # PrevRgstn variables
  orgNm_all = ''
  orgPK_all = ''
  regBeginDt_all = ''
  regEndDt_all = ''

  # PrevRgstn BrnchOfLoc variables
  city_all = ''
  state_all = ''

  # EmpHs variables
  EmpHs_fromDt_all = ''
  EmpHs_toDt_all = ''
  EmpHs_orgNm_all = ''
  EmpHs_city_all = ''
  EmpHs_state_all = ''

  tree=Xet.parse( 'sample.xml' )
  root=tree.getroot()
  Indvls = list(root[0])
  Indvl = list(Indvls)

  for Indvl_child in Indvl:
    
    # Loop for Info Tag
    for idx, child in enumerate(Indvl_child):
      
      keys = child.attrib.keys()
      
      if len(keys) != 0:
        for k in keys:
          if k == 'lastNm':
            Info_lastNm.append(child.attrib[k] if (child.attrib[k] is not None) or (child.attrib[k] != ' ') else 'None')
            print(f'{k}: {child.attrib[k]}\n')

          elif k == 'firstNm':
            Info_firstNm.append(child.attrib[k] if (child.attrib[k] is not None) or (child.attrib[k] != ' ') else 'None')
            print(f'{k}: {child.attrib[k]}\n')

          elif k == 'midNm':
            Info_midNm.append(child.attrib[k] if (child.attrib[k] is not None) or (child.attrib[k] != ' ') else 'None')
            print(f'{k}: {child.attrib[k]}\n')

          elif k == 'indvlPK':
            Info_indvlPK.append(child.attrib[k] if (child.attrib[k] is not None) or (child.attrib[k] != ' ') else 'None')
            print(f'{k}: {child.attrib[k]}\n')

          elif k == 'actvAGReg':
            Info_actvAGReg.append(child.attrib[k] if (child.attrib[k] is not None) or (child.attrib[k] != ' ') else 'None')
            print(f'{k}: {child.attrib[k]}\n')

          elif k == 'link':
            Info_link.append(child.attrib[k] if (child.attrib[k] is not None) or (child.attrib[k] != ' ') else 'None')
            print(f'{k}: {child.attrib[k]}\n')

    # Loop for OthrNms Tag
    OthrNms_child = list(Indvl_child[1])

    for child in OthrNms_child:
      
      keys = child.attrib.keys()
      
      if len(keys) != 0:
        for k in keys:

          if k == 'lastNm':
            OthrNm_lastNm.append(child.attrib[k] if (child.attrib[k] is not None) or (child.attrib[k] != ' ') else 'None')
            print(f'{k}: {child.attrib[k]}\n')

          elif k == 'firstNm':
            OthrNm_firstNm.append(child.attrib[k] if (child.attrib[k] is not None) or (child.attrib[k] != ' ') else 'None')
            print(f'{k}: {child.attrib[k]}\n')

    # Loop for CrntEmps Tag
    CrntEmps_child = list(Indvl_child[2])

    for child in CrntEmps_child:
      
      keys = child.attrib.keys()
      
      if len(keys) != 0:
        for k in keys:

          if k == 'orgNm':
            CrntEmp_orgNm.append(child.attrib[k] if (child.attrib[k] is not None) or (child.attrib[k] != ' ') else 'None')
            print(f'{k}: {child.attrib[k]}\n')

          elif k == 'orgPK':
            CrntEmp_orgPK.append(child.attrib[k] if (child.attrib[k] is not None) or (child.attrib[k] != ' ') else 'None')
            print(f'{k}: {child.attrib[k]}\n')

          elif k == 'str1':
            CrntEmp_str1.append(child.attrib[k] if (child.attrib[k] is not None) or (child.attrib[k] != ' ') else 'None')
            print(f'{k}: {child.attrib[k]}\n')

          elif k == 'city':
            CrntEmp_city.append(child.attrib[k] if (child.attrib[k] is not None) or (child.attrib[k] != ' ') else 'None')
            print(f'{k}: {child.attrib[k]}\n')

          elif k == 'state':
            CrntEmp_state.append(child.attrib[k] if (child.attrib[k] is not None) or (child.attrib[k] != ' ') else 'None')
            print(f'{k}: {child.attrib[k]}\n')

          elif k == 'cntry':
            CrntEmp_cntry.append(child.attrib[k] if (child.attrib[k] is not None) or (child.attrib[k] != ' ') else 'None')
            print(f'{k}: {child.attrib[k]}\n')

          elif k == 'postlCd':
            CrntEmp_postlCd.append(child.attrib[k] if (child.attrib[k] is not None) or (child.attrib[k] != ' ') else 'None')
            print(f'{k}: {child.attrib[k]}\n')

      # Loop for CrntEmp child nodes
      CrntEmp = list(child)

      if len(CrntEmp) != 0:

        for CrntEmp_child in CrntEmp:

          CrntEmp_child_nodes = list(CrntEmp_child)

          for nodes in CrntEmp_child_nodes:

            keys = nodes.attrib.keys()
        
            if len(keys) != 0:
              for k in keys:
                if k == 'regAuth':
                  regAuth_all += nodes.attrib[k] + ',\n'
                  print(f'{k}: {nodes.attrib[k]}\n')

                elif k == 'regCat':
                  regCat_all += nodes.attrib[k] + ',\n'
                  print(f'{k}: {nodes.attrib[k]}\n')

                elif k == 'st':
                  st_all += nodes.attrib[k] + ',\n'
                  print(f'{k}: {nodes.attrib[k]}\n')

                elif k == 'stDt':
                  stDt_all += nodes.attrib[k] + ',\n'
                  print(f'{k}: {nodes.attrib[k]}\n')

                elif k == 'str1':
                  str1_all += nodes.attrib[k] + ',\n'
                  print(f'{k}: {nodes.attrib[k]}\n')

                elif k == 'city':
                  city_all += nodes.attrib[k] + ',\n'
                  print(f'{k}: {nodes.attrib[k]}\n')

                elif k == 'state':
                  state_all += nodes.attrib[k] + ',\n'
                  print(f'{k}: {nodes.attrib[k]}\n')

                elif k == 'cntry':
                  cntry_all += nodes.attrib[k] + ',\n'
                  print(f'{k}: {nodes.attrib[k]}\n')

                elif k == 'postlCd':
                  postlCd_all += nodes.attrib[k] + ',\n'
                  print(f'{k}: {nodes.attrib[k]}\n')

        CrntRgstn_regAuth.append(regAuth_all)
        CrntRgstn_regCat.append(regCat_all)
        CrntRgstn_st.append(st_all)
        CrntRgstn_stDt.append(stDt_all)

        BrnchOfLoc_str1.append(str1_all)
        BrnchOfLoc_city.append(city_all)
        BrnchOfLoc_state.append(state_all)
        BrnchOfLoc_cntry.append(cntry_all)
        BrnchOfLoc_postlCd.append(postlCd_all)
      
      else:
        CrntRgstn_regAuth.append('None')
        CrntRgstn_regCat.append('None')
        CrntRgstn_st.append('None')
        CrntRgstn_stDt.append('None')

        BrnchOfLoc_str1.append('None')
        BrnchOfLoc_city.append('None')
        BrnchOfLoc_state.append('None')
        BrnchOfLoc_cntry.append('None')
        BrnchOfLoc_postlCd.append('None')

    # Loop for Exms Tag
    Exms = list(Indvl_child[3])

    if len(Exms) != 0:

      for child in Exms:
        
        keys = child.attrib.keys()
        
        if len(keys) != 0:
          for k in keys:
            if k == 'exmCd':
              exmCd_all += child.attrib[k] + ',\n'
              print(f'{k}: {child.attrib[k]}\n')

            elif k == 'exmNm':
              exmNm_all += child.attrib[k] + ',\n'
              print(f'{k}: {child.attrib[k]}\n')

            elif k == 'exmDt':
              exmDt_all += child.attrib[k] + ',\n'
              print(f'{k}: {child.attrib[k]}\n')

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
              print(f'{k}: {child.attrib[k]}\n')
    else:
      Dsgntn_dsgntnNm.append('None')
    
    # Loop for PrevRgstns Tag
    PrevRgstns = list(Indvl_child[5])

    if len(PrevRgstns) != 0:
      
      for child in PrevRgstns:
        
        keys = child.attrib.keys()
        
        if len(keys) != 0:
          for k in keys:
            if k == 'orgNm':
              orgNm_all += child.attrib[k] + ',\n'
              print(f'{k}: {child.attrib[k]}\n')

            elif k == 'orgPK':
              orgPK_all += child.attrib[k] + ',\n'
              print(f'{k}: {child.attrib[k]}\n')

            elif k == 'regBeginDt':
              regBeginDt_all += child.attrib[k] + ',\n'
              print(f'{k}: {child.attrib[k]}\n')

            elif k == 'regEndDt':
              regEndDt_all += child.attrib[k] + ',\n'
              print(f'{k}: {child.attrib[k]}\n')

        # Loop for PrevRgstn_branchloc Tag
        PrevRgstn_branchloc = list(child)

        PrevRgstn_branchloc_nodes = list(PrevRgstn_branchloc)

        if len(PrevRgstn_branchloc_nodes) != 0:

          for node in PrevRgstn_branchloc_nodes:

            items = list(node)

            for item in items:
            
              keys = item.attrib.keys()

              if len(keys) != 0:
                for k in keys:
                  if k == 'city':
                    city_all += item.attrib[k] + ',\n'
                    print(f'{k}: {item.attrib[k]}\n')

                  elif k == 'state':
                    state_all += item.attrib[k] + ',\n'
                    print(f'{k}: {item.attrib[k]}\n')

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

    if len(EmpHss) != 0:
      for child in EmpHss:
        
        keys = child.attrib.keys()

        if len(keys) != 0:
          for k in keys:
            if k == 'fromDt':
              EmpHs_fromDt_all += child.attrib[k] + ',\n'
              print(f'{k}: {child.attrib[k]}\n')

            elif k == 'toDt':
              EmpHs_toDt_all += child.attrib[k] + ',\n'
              print(f'{k}: {child.attrib[k]}\n')

            elif k == 'orgNm':
              EmpHs_orgNm_all += child.attrib[k] + ',\n'
              print(f'{k}: {child.attrib[k]}\n')

            elif k == 'city':
              EmpHs_city_all += child.attrib[k] + ',\n'
              print(f'{k}: {child.attrib[k]}\n')

            elif k == 'state':
              EmpHs_state_all += child.attrib[k] + ',\n'
              print(f'{k}: {child.attrib[k]}\n')

            # Check if attribute toDt exist
            if 'toDt' in keys:
              pass
            else:
              EmpHs_toDt_all += 'None,\n'
              print(f'toDt : None \n')

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


  time_end = datetime.datetime.now().replace(microsecond=0)
  runtime = time_end - time_start
  print(f"Script runtime: {runtime}.")

  # Save scraped URLs to a CSV file
  now = datetime.datetime.now().strftime('%Y%m%d-%Hh%M')
  print('Saving to a CSV file...')

  data = {'lastNm': Info_lastNm, 'firstNm': Info_firstNm, 'midNm': Info_midNm, 'indvlPK': Info_indvlPK, 'actvAGReg': Info_actvAGReg, 'link': Info_link, 'OthrNm lastNm': OthrNm_lastNm, 'OthrNm firstNm': OthrNm_firstNm, 'CrntEmp orgNm': CrntEmp_orgNm, 'CrntEmp orgPK': CrntEmp_orgPK, 'CrntEmp str1': CrntEmp_str1, 'CrntEmp city': CrntEmp_city, 'CrntEmp state': CrntEmp_state, 'CrntEmp cntry': CrntEmp_cntry, 'CrntEmp postlCd': CrntEmp_postlCd, 'CrntRgstn regAuth': CrntRgstn_regAuth, 'CrntRgstn regCat': CrntRgstn_regCat, 'CrntRgstn st': CrntRgstn_st, 'CrntRgstn stDt': CrntRgstn_stDt, 'BrnchOfLoc str1': BrnchOfLoc_str1, 'BrnchOfLoc city': BrnchOfLoc_city, 'BrnchOfLoc state': BrnchOfLoc_state, 'BrnchOfLoc cntry': BrnchOfLoc_cntry, 'BrnchOfLoc postlCd': BrnchOfLoc_postlCd, 'exmCd': Exm_exmCd, 'exmNm': Exm_exmNm, 'exmDt': Exm_exmDt, 'dsgntnNm': Dsgntn_dsgntnNm, 'PrevRgstn_orgNm': PrevRgstn_orgNm, 'PrevRgstn orgPK': PrevRgstn_orgPK, 'PrevRgstn regBeginDt': PrevRgstn_regBeginDt, 'PrevRgstn regEndDt': PrevRgstn_regEndDt, 'PrevRgstn branchloc city': PrevRgstn_branchloc_city, 'PrevRgstn branchloc state': PrevRgstn_branchloc_state, 'EmpHs fromDt': EmpHs_fromDt, 'EmpHs toDt': EmpHs_toDt, 'EmpHs orgNm': EmpHs_orgNm, 'EmpHs city': EmpHs_city, 'EmpHs state': EmpHs_state}

  df=pd.DataFrame(data=data)
  df.index+=1
  directory = os.path.dirname(os.path.realpath(__file__))
  filename = "convertedXML" + now + ".csv"
  file_path = os.path.join(directory,'csvfiles/', filename)
  df.to_csv(file_path)

  print('Your files are ready.')

if __name__ == '__main__':
    convert()
from edc_locator.action_items import SubjectLocatorAction

from edc_action_item import Action, site_action_items, HIGH_PRIORITY

MATERNALOFF_STUDY_ACTION = 'submit-maternaloff-study'
CAREGIVER_LOCATOR_ACTION = 'submit-caregiver-locator'
ULTRASOUND_ACTION = 'submit-ultrasound'
MATERNAL_DELIVERY_ACTION = 'submit-maternal-delivery'
MATERNAL_COVID_SCREENING_ACTION = 'update-maternal-covid-results'


class MaternalOffStudyAction(Action):
    name = MATERNALOFF_STUDY_ACTION
    display_name = 'Submit Maternal Offstudy'
    reference_model = 'td_prn.maternaloffstudy'
    admin_site_name = 'td_prn_admin'
    priority = HIGH_PRIORITY
    singleton = True


class CaregiverLocatorAction(SubjectLocatorAction):
    name = CAREGIVER_LOCATOR_ACTION
    display_name = 'Submit Caregiver Locator'
    reference_model = 'flourish_caregiver.caregiverlocator'
    admin_site_name = 'flourish_caregiver_admin'


class MaternalUltrasoundAction(Action):
    name = ULTRASOUND_ACTION
    display_name = 'Submit Maternal Ultrasound'
    reference_model = 'flourish_caregiver.maternalultrasoundinitial'
    admin_site_name = 'flourish_caregiver_admin'
    create_by_user = False

    def get_next_actions(self):
        actions = []

        # resave visit to update metadata
        self.reference_model_obj.maternal_visit.save()

        if self.reference_model_obj.number_of_gestations != '1':
            actions = [MaternalOffStudyAction]
        else:
            self.delete_if_new(MaternalOffStudyAction)
        return actions


class MaternalLabourDeliveryAction(Action):
    name = MATERNAL_DELIVERY_ACTION
    display_name = 'Submit Maternal Delivery'
    reference_model = 'flourish_caregiver.maternallabourdel'
    admin_site_name = 'flourish_caregiver_admin'
    priority = HIGH_PRIORITY

    def get_next_actions(self):
        actions = []
        if self.reference_model_obj.live_infants_to_register != 1:
            actions = [MaternalOffStudyAction]
        return actions


class MaternalCovidScreeningAction(Action):
    name = MATERNAL_COVID_SCREENING_ACTION
    display_name = 'Update Maternal Covid Screening Test Results'
    reference_model = 'flourish_caregiver.maternalcovidscreening'
    admin_site_name = 'flourish_caregiver_admin'
    priority = HIGH_PRIORITY

    def close_action_item_on_save(self):
        """Returns True if action item for \'action_identifier\'
        is to be closed on post_save.
        """
        return self.reference_model_obj.covid_results != 'pending'


# site_action_items.register(CaregiverLocatorAction)

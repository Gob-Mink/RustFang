Feature: Sequencer control
  Scenario: Starting the sequencer
    When I press play
    Then I see the sequencer start
    When I press stop 
    Then I see the sequencer stop
package cs320_Project_Milestone_Ryan_Blackburn_v2;

import static org.junit.jupiter.api.Assertions.*;

import java.util.Date;

import org.junit.jupiter.api.Test;

public class AppointmentTest {

    // Helper methods for dates
    private Date getFutureDate() {                              // 1 hour in the future
        return new Date(System.currentTimeMillis() + 3_600_000L);
    }

    private Date getPastDate() {                                // 1 hour in the past
        return new Date(System.currentTimeMillis() - 3_600_000L);
    }

    @Test
    void testValidAppointmentCreation() {                       // Valid constructor
        Date futureDate = getFutureDate();
        Appointment appt = new Appointment("A001", futureDate, "Checkup with doctor");

        assertEquals("A001", appt.getAppointmentId());
        assertEquals(futureDate, appt.getAppointmentDate());
        assertEquals("Checkup with doctor", appt.getDescription());
    }

    @Test
    void testAppointmentIdNull() {                              // Null ID
        Date futureDate = getFutureDate();
        assertThrows(IllegalArgumentException.class, () -> {
            new Appointment(null, futureDate, "Dentist visit");
        });
    }

    @Test
    void testAppointmentIdTooLong() {                           // Too-long ID
        Date futureDate = getFutureDate();
        String longId = "12345678901";                          // 11 characters
        assertTrue(longId.length() > 10);

        assertThrows(IllegalArgumentException.class, () -> {
            new Appointment(longId, futureDate, "Dentist visit");
        });
    }

    @Test
    void testAppointmentDateNull() {                            // Null date
        assertThrows(IllegalArgumentException.class, () -> {
            new Appointment("A001", null, "Dentist visit");
        });
    }

    @Test
    void testAppointmentDateInPast() {                          // Date in the past
        Date pastDate = getPastDate();
        assertThrows(IllegalArgumentException.class, () -> {
            new Appointment("A001", pastDate, "Dentist visit");
        });
    }

    @Test
    void testDescriptionNull() {                                // Null description
        Date futureDate = getFutureDate();
        assertThrows(IllegalArgumentException.class, () -> {
            new Appointment("A001", futureDate, null);
        });
    }

    @Test
    void testDescriptionTooLong() {                             // Too-long description
        Date futureDate = getFutureDate();
        String longDescription = "This description is definitely going to be longer "
                + "than fifty characters in order to trigger an error.";
        assertTrue(longDescription.length() > 50);

        assertThrows(IllegalArgumentException.class, () -> {
            new Appointment("A001", futureDate, longDescription);
        });
    }

    // === Setter tests ===

    @Test
    void testSetAppointmentDateValid() {                        // Valid date update
        Date futureDate = getFutureDate();
        Appointment appt = new Appointment("A001", futureDate, "Checkup");

        Date laterFutureDate = new Date(System.currentTimeMillis() + 7_200_000L);
        appt.setAppointmentDate(laterFutureDate);

        assertEquals(laterFutureDate, appt.getAppointmentDate());
    }

    @Test
    void testSetAppointmentDateNull() {                         // Null date in setter
        Date futureDate = getFutureDate();
        Appointment appt = new Appointment("A001", futureDate, "Checkup");

        assertThrows(IllegalArgumentException.class, () -> {
            appt.setAppointmentDate(null);
        });
    }

    @Test
    void testSetAppointmentDateInPast() {                       // Past date in setter
        Date futureDate = getFutureDate();
        Appointment appt = new Appointment("A001", futureDate, "Checkup");

        Date pastDate = getPastDate();
        assertThrows(IllegalArgumentException.class, () -> {
            appt.setAppointmentDate(pastDate);
        });
    }

    @Test
    void testSetDescriptionValid() {                            // Valid description update
        Date futureDate = getFutureDate();
        Appointment appt = new Appointment("A001", futureDate, "Checkup");

        appt.setDescription("Updated description");
        assertEquals("Updated description", appt.getDescription());
    }

    @Test
    void testSetDescriptionNull() {                             // Null description in setter
        Date futureDate = getFutureDate();
        Appointment appt = new Appointment("A001", futureDate, "Checkup");

        assertThrows(IllegalArgumentException.class, () -> {
            appt.setDescription(null);
        });
    }
}

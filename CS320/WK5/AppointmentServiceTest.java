package cs320_Project_Milestone_Ryan_Blackburn_v2;

import static org.junit.jupiter.api.Assertions.*;

import java.util.Date;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

public class AppointmentServiceTest {

    private AppointmentService appointmentService;

    @BeforeEach
    void setUp() {                                              // Initialize service before each test
        appointmentService = new AppointmentService();
    }

    private Date getFutureDate() {                              // 1 hour in the future
        return new Date(System.currentTimeMillis() + 3_600_000L);
    }

    @Test
    void testAddAppointmentValid() {                            // Valid add
        Date futureDate = getFutureDate();
        appointmentService.addAppointment("A001", futureDate, "Checkup");

        Appointment appt = appointmentService.getAppointment("A001");
        assertNotNull(appt);
        assertEquals("A001", appt.getAppointmentId());
        assertEquals("Checkup", appt.getDescription());
    }

    @Test
    void testAddAppointmentNullIdThrowsException() {            // Null ID in add
        Date futureDate = getFutureDate();

        assertThrows(IllegalArgumentException.class, () -> {
            appointmentService.addAppointment(null, futureDate, "Checkup");
        });
    }

    @Test
    void testAddDuplicateAppointmentThrowsException() {         // Duplicate ID in add
        Date futureDate = getFutureDate();

        appointmentService.addAppointment("A001", futureDate, "Checkup");

        assertThrows(IllegalArgumentException.class, () -> {
            appointmentService.addAppointment("A001", futureDate, "Another Checkup");
        });
    }

    @Test
    void testDeleteAppointmentValid() {                         // Valid delete
        Date futureDate = getFutureDate();
        appointmentService.addAppointment("A001", futureDate, "Checkup");

        appointmentService.deleteAppointment("A001");

        Appointment appt = appointmentService.getAppointment("A001");
        assertNull(appt);
    }

    @Test
    void testDeleteNonexistentAppointmentThrowsException() {    // Delete non-existing ID
        assertThrows(IllegalArgumentException.class, () -> {
            appointmentService.deleteAppointment("DOES_NOT_EXIST");
        });
    }

    @Test
    void testDeleteAppointmentNullIdThrowsException() {         // Null ID in delete
        assertThrows(IllegalArgumentException.class, () -> {
            appointmentService.deleteAppointment(null);
        });
    }
}

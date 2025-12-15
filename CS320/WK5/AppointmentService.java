package main;

import java.util.Date;
import java.util.HashMap;
import java.util.Map;

public class AppointmentService {

    private final Map<String, Appointment> appointments = new HashMap<>();

    public void addAppointment(String appointmentId, Date appointmentDate, String description) {        //Add new appointment if ID unique
        if (appointmentId == null) {
            throw new IllegalArgumentException("Appointment ID cannot be null");
        }

        if (appointments.containsKey(appointmentId)) {
            throw new IllegalArgumentException("Appointment ID already exists");
        }

        Appointment newAppointment = new Appointment(appointmentId, appointmentDate, description);
        appointments.put(appointmentId, newAppointment);
    }

    public void deleteAppointment(String appointmentId) {                                               //Delete by ID
        if (appointmentId == null || !appointments.containsKey(appointmentId)) {
            throw new IllegalArgumentException("Appointment ID does not exist");
        }
        appointments.remove(appointmentId);
    }

    public Appointment getAppointment(String appointmentId) {                                   //Testing verification helper, gets appointment by ID
        return appointments.get(appointmentId);
    }
}

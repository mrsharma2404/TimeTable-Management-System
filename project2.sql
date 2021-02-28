-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 28, 2021 at 07:57 PM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.2.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `project2`
--

-- --------------------------------------------------------

--
-- Table structure for table `record`
--

CREATE TABLE `record` (
  `faculty_name` varchar(50) NOT NULL,
  `faculty_id` varchar(50) NOT NULL,
  `image` varchar(100) NOT NULL,
  `dob` date NOT NULL,
  `mobile` int(20) NOT NULL,
  `address` varchar(200) NOT NULL,
  `join_date` date NOT NULL,
  `salary` varchar(20) NOT NULL,
  `qualification` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `record`
--

INSERT INTO `record` (`faculty_name`, `faculty_id`, `image`, `dob`, `mobile`, `address`, `join_date`, `salary`, `qualification`) VALUES
('asd', '12', 'PC_GALLERY_218.jpg', '2020-12-23', 123, 'ghj', '2020-12-22', '123', 'hjk'),
('asd', '12', 'wallpper1.jpg', '2020-12-23', 123, 'ghj', '2020-12-22', '123', 'hjk'),
('abcd', '', 'l6.jpeg', '0000-00-00', 0, '', '0000-00-00', '', ''),
('Iron Man', '123dontrequired', 'l4.jpg', '1986-01-07', 2147483647, 'NewYork', '2021-01-01', '1,000,000,000', 'Engineer'),
('Mr. DD Shrivastav', 'dd456', 'l4.jpg', '1989-02-09', 2147483647, 'Rajeev Plaza', '2015-01-14', '30,000 Rs.', 'Msc. ');

-- --------------------------------------------------------

--
-- Table structure for table `timetable`
--

CREATE TABLE `timetable` (
  `faculty_name` varchar(50) NOT NULL,
  `date` varchar(10) NOT NULL,
  `day` varchar(10) NOT NULL,
  `time` varchar(20) NOT NULL,
  `classroom` varchar(10) NOT NULL,
  `course` varchar(20) NOT NULL,
  `semester` varchar(20) NOT NULL,
  `batch` varchar(50) NOT NULL,
  `subject_code` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `timetable`
--

INSERT INTO `timetable` (`faculty_name`, `date`, `day`, `time`, `classroom`, `course`, `semester`, `batch`, `subject_code`) VALUES
('Mr Gaurav Dubey', 'null', 'Monday', '11:00 to 12:00', 'online', 'B.tech', 'Fifth Semester', 'Computer Science Engineering III', 'CS-501'),
('Mr Gaurav Dubey', 'null', 'Wednesday', '11:00 to 12:00', 'online', 'B.tech', 'Fifth Semester', 'Computer Science Engineering III', 'CS-501'),
('Mr Gaurav Dubey', 'null', 'Thursday', '11:00 to 12:00', 'online', 'B.tech', 'Fifth Semester', 'Computer Science Engineering III', 'CS-501'),
('Mr Gaurav Dubey', 'null', 'Saturday', '11:00 to 12:00', 'online', 'B.tech', 'Fifth Semester', 'Computer Science Engineering III', 'CS-501'),
('Mr Kuldeep Jadon', 'null', 'Tuesday', '01:00 to 02:00', 'online', 'B.tech', 'Fifth Semester', 'Computer Science Engineering III', 'CS-502'),
('Mr Kuldeep Jadon', 'null', 'Thursday', '12:00 to 01:00', 'online', 'B.tech', 'Fifth Semester', 'Computer Science Engineering III', 'CS-502'),
('Mr Kuldeep Jadon', 'null', 'Friday', '01:00 to 02:00', 'online', 'B.tech', 'Fifth Semester', 'Computer Science Engineering III', 'CS-502'),
('Mr DD Shrivastava', 'null', 'Monday', '12:00 to 01:00', 'online', 'B.tech', 'Fifth Semester', 'Computer Science Engineering III', 'CS-503'),
('Mr DD Shrivastava', 'null', 'Wednesday', '01:00 to 02:00', 'online', 'B.tech', 'Fifth Semester', 'Computer Science Engineering III', 'CS-503'),
('Mr DD Shrivastava', 'null', 'Friday', '12:00 to 01:00', 'online', 'B.tech', 'Fifth Semester', 'Computer Science Engineering III', 'CS-503'),
('Mr DD Shrivastava', 'null', 'Saturday', '12:00 to 01:00', 'online', 'B.tech', 'Fifth Semester', 'Computer Science Engineering III', 'CS-503'),
('Mrs Deepika Saraswat', 'null', 'Tuesday', '11:00 to 12:00', 'online', 'B.tech', 'Fifth Semester', 'Computer Science Engineering III', 'CS-504'),
('Mrs Deepika Saraswat', 'null', 'Wednesday', '12:00 to 01:00', 'online', 'B.tech', 'Fifth Semester', 'Computer Science Engineering III', 'CS-504'),
('Mrs Deepika Saraswat', 'null', 'Thursday', '11:00 to 12:00', 'online', 'B.tech', 'Fifth Semester', 'Computer Science Engineering III', 'CS-504'),
('Mrs Deepika Saraswat', 'null', 'Friday', '11:00 to 12:00', 'online', 'B.tech', 'Fifth Semester', 'Computer Science Engineering III', 'CS-504'),
('Mr Nitin Dixit', 'null', 'Monday', '01:00 to 02:00', 'online', 'B.tech', 'Fifth Semester', 'Computer Science Engineering III', 'CS-505'),
('Mr Nitin Dixit', 'null', 'Saturday', '01:00 to 02:00', 'online', 'B.tech', 'Fifth Semester', 'Computer Science Engineering III', 'CS-505'),
('Mr Jitendra Kushwah', 'null', 'Tuesday', '12:00 to 01:00', 'online', 'B.tech', 'Fifth Semester', 'Computer Science Engineering III', 'CS-506'),
('Mr Jitendra Kushwah', 'null', 'Thursday', '01:00 to 02:00', 'online', 'B.tech', 'Fifth Semester', 'Computer Science Engineering III', 'CS-506'),
('Mrs Deepika Saraswat', 'null', 'Monday', '01:00 to 02:00', 'online', 'B.tech', 'Third Semester', 'Computer Science Engineering III', 'cs-305'),
('Mrs Deepika Saraswat', 'null', 'Monday', '12:00 to 01:00', '', 'B.tech', 'First Semester', 'Computer Science Engineering I', '');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
